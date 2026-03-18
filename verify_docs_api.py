"""
Crazyrouter 文档 API 一致性验证脚本
验证文档中描述的端点是否与线上 API 实际行为一致

用法:
  python verify_docs_api.py

需要环境变量或直接修改下方配置:
  API_BASE_URL - API 基础地址
  API_KEY      - sk- 开头的 API Key
  ACCESS_TOKEN - 用户 Access Token (控制台接口用)
  USER_ID      - 用户 ID (控制台接口用)
"""

import requests
import json
import sys
import os
from datetime import datetime

# Windows 控制台 UTF-8
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ============ 配置 ============
API_BASE = os.getenv("API_BASE_URL", "https://crazyrouter.com")
API_KEY = os.getenv("API_KEY", "")           # sk-xxx
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "") # 控制台 API 用
USER_ID = os.getenv("USER_ID", "1")

HEADERS_RELAY = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

HEADERS_MGMT = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "New-Api-User": USER_ID,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# ============ 结果收集 ============
results = []

def log_result(category, endpoint, method, status, detail, match=True):
    icon = "✅" if match else "❌"
    results.append({
        "category": category,
        "endpoint": endpoint,
        "method": method,
        "status": status,
        "detail": detail,
        "match": match
    })
    print(f"  {icon} [{method}] {endpoint} → {status} {detail}")

def section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

# ============ 1. 公开端点（无需认证） ============
def test_public_endpoints():
    section("1. 公开端点 (文档: quickstart.mdx, api-endpoint.mdx)")

    public_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    # GET /api/status — 文档: introduction.mdx 提到的系统状态
    try:
        r = requests.get(f"{API_BASE}/api/status", headers=public_headers, timeout=10)
        ok = r.status_code == 200
        log_result("公开", "/api/status", "GET", r.status_code,
                   "系统状态正常" if ok else f"异常: {r.text[:100]}", ok)
    except Exception as e:
        log_result("公开", "/api/status", "GET", 0, str(e), False)

    # GET /api/pricing — 文档: quickstart.mdx 提到的定价接口
    try:
        r = requests.get(f"{API_BASE}/api/pricing", headers=public_headers, timeout=10)
        ok = r.status_code == 200
        data = r.json() if ok else {}
        count = len(data.get("data", [])) if isinstance(data.get("data"), list) else "N/A"
        log_result("公开", "/api/pricing", "GET", r.status_code,
                   f"返回 {count} 个模型定价" if ok else f"异常: {r.text[:100]}", ok)
    except Exception as e:
        log_result("公开", "/api/pricing", "GET", 0, str(e), False)

    # GET /v1/models — 文档: chat/openai/models.mdx
    try:
        r = requests.get(f"{API_BASE}/v1/models", headers=HEADERS_RELAY, timeout=10)
        ok = r.status_code == 200
        data = r.json() if ok else {}
        count = len(data.get("data", [])) if isinstance(data.get("data"), list) else "N/A"
        log_result("公开", "/v1/models", "GET", r.status_code,
                   f"返回 {count} 个模型" if ok else f"需要认证或异常", ok)
    except Exception as e:
        log_result("公开", "/v1/models", "GET", 0, str(e), False)

# ============ 2. Chat API（文档: chat/openai/completions.mdx） ============
def test_chat_api():
    section("2. Chat API (文档: chat/openai/completions.mdx)")

    if not API_KEY:
        print("  ⚠️  跳过: 未设置 API_KEY")
        return

    # POST /v1/chat/completions — 非流式
    try:
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": "Say 'doc-test-ok' and nothing else."}],
            "max_tokens": 20
        }
        r = requests.post(f"{API_BASE}/v1/chat/completions",
                          headers=HEADERS_RELAY, json=payload, timeout=30)
        ok = r.status_code == 200
        data = r.json() if ok else {}
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")[:50]
        usage = data.get("usage", {})
        log_result("Chat", "/v1/chat/completions", "POST", r.status_code,
                   f"回复: {content} | tokens: {usage.get('total_tokens', '?')}" if ok
                   else f"错误: {r.text[:100]}", ok)
    except Exception as e:
        log_result("Chat", "/v1/chat/completions", "POST", 0, str(e), False)

    # POST /v1/chat/completions — 流式 (只验证能收到 SSE)
    try:
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": "Say 'stream-ok'"}],
            "max_tokens": 10,
            "stream": True
        }
        r = requests.post(f"{API_BASE}/v1/chat/completions",
                          headers=HEADERS_RELAY, json=payload, timeout=30, stream=True)
        first_line = ""
        for line in r.iter_lines():
            if line:
                first_line = line.decode("utf-8", errors="replace")
                break
        ok = r.status_code == 200 and first_line.startswith("data:")
        log_result("Chat", "/v1/chat/completions (stream)", "POST", r.status_code,
                   f"SSE 首行: {first_line[:60]}" if ok else f"非 SSE: {first_line[:60]}", ok)
        r.close()
    except Exception as e:
        log_result("Chat", "/v1/chat/completions (stream)", "POST", 0, str(e), False)

# ============ 3. 图像 API（文档: images/gpt-image.mdx, images/dalle.mdx） ============
def test_image_api():
    section("3. 图像 API (文档: images/gpt-image.mdx)")

    if not API_KEY:
        print("  ⚠️  跳过: 未设置 API_KEY")
        return

    # POST /v1/images/generations — 只验证端点可达和参数格式
    try:
        payload = {
            "model": "dall-e-3",
            "prompt": "A white cat, simple sketch",
            "n": 1,
            "size": "1024x1024"
        }
        r = requests.post(f"{API_BASE}/v1/images/generations",
                          headers=HEADERS_RELAY, json=payload, timeout=60)
        # 200=成功, 402=余额不足, 400=参数错误 都说明端点存在
        ok = r.status_code in (200, 402, 400, 429)
        data = r.json() if r.status_code == 200 else {}
        if r.status_code == 200:
            url = data.get("data", [{}])[0].get("url", "")[:60]
            detail = f"图片URL: {url}..."
        else:
            detail = f"端点可达, 返回: {r.text[:80]}"
        log_result("图像", "/v1/images/generations", "POST", r.status_code, detail, ok)
    except Exception as e:
        log_result("图像", "/v1/images/generations", "POST", 0, str(e), False)

# ============ 4. 音频 API（文档: audio/tts.mdx） ============
def test_audio_api():
    section("4. 音频 API (文档: audio/tts.mdx)")

    if not API_KEY:
        print("  ⚠️  跳过: 未设置 API_KEY")
        return

    # POST /v1/audio/speech — TTS
    try:
        payload = {
            "model": "tts-1",
            "input": "Hello",
            "voice": "alloy"
        }
        r = requests.post(f"{API_BASE}/v1/audio/speech",
                          headers=HEADERS_RELAY, json=payload, timeout=30)
        ok = r.status_code in (200, 402, 400, 429)
        if r.status_code == 200:
            detail = f"返回音频 {len(r.content)} bytes, Content-Type: {r.headers.get('Content-Type', '?')}"
        else:
            detail = f"端点可达, 返回: {r.text[:80]}"
        log_result("音频", "/v1/audio/speech", "POST", r.status_code, detail, ok)
    except Exception as e:
        log_result("音频", "/v1/audio/speech", "POST", 0, str(e), False)

# ============ 5. 嵌入 API（文档: embeddings/create.mdx） ============
def test_embeddings_api():
    section("5. 嵌入 API (文档: embeddings/create.mdx)")

    if not API_KEY:
        print("  ⚠️  跳过: 未设置 API_KEY")
        return

    try:
        payload = {
            "model": "text-embedding-3-small",
            "input": "Hello world"
        }
        r = requests.post(f"{API_BASE}/v1/embeddings",
                          headers=HEADERS_RELAY, json=payload, timeout=30)
        ok = r.status_code in (200, 402, 400, 429)
        data = r.json() if r.status_code == 200 else {}
        if r.status_code == 200:
            dim = len(data.get("data", [{}])[0].get("embedding", []))
            detail = f"向量维度: {dim}"
        else:
            detail = f"端点可达, 返回: {r.text[:80]}"
        log_result("嵌入", "/v1/embeddings", "POST", r.status_code, detail, ok)
    except Exception as e:
        log_result("嵌入", "/v1/embeddings", "POST", 0, str(e), False)

# ============ 6. API Key / 控制台接口（文档: token-management/*.mdx） ============
def test_token_management():
    section("6. API Key / 控制台接口 (文档: token-management/list.mdx)")

    if not ACCESS_TOKEN:
        print("  ⚠️  跳过: 未设置 ACCESS_TOKEN")
        return

    # GET /api/token/ — 获取令牌列表
    try:
        r = requests.get(f"{API_BASE}/api/token/?p=0&size=5",
                         headers=HEADERS_MGMT, timeout=10)
        ok = r.status_code == 200
        data = r.json() if ok else {}
        if ok and data.get("success"):
            count = len(data.get("data", {}).get("items", []))
            detail = f"返回 {count} 个令牌"
        else:
            detail = f"返回: {r.text[:80]}"
            ok = False
        log_result("Token管理", "/api/token/", "GET", r.status_code, detail, ok)
    except Exception as e:
        log_result("Token管理", "/api/token/", "GET", 0, str(e), False)

    # GET /api/token/search — 搜索令牌
    try:
        r = requests.get(f"{API_BASE}/api/token/search?keyword=test",
                         headers=HEADERS_MGMT, timeout=10)
        ok = r.status_code == 200
        log_result("Token管理", "/api/token/search", "GET", r.status_code,
                   "搜索端点可达" if ok else f"返回: {r.text[:80]}", ok)
    except Exception as e:
        log_result("Token管理", "/api/token/search", "GET", 0, str(e), False)

# ============ 7. 视频 API（文档: video/unified.mdx）— 仅验证端点可达 ============
def test_video_api():
    section("7. 视频 API (文档: video/unified.mdx) — 仅验证端点存在")

    if not API_KEY:
        print("  ⚠️  跳过: 未设置 API_KEY")
        return

    # POST /v1/video/create — 发送最小 payload 验证端点存在
    try:
        payload = {"model": "test-nonexistent", "prompt": "test"}
        r = requests.post(f"{API_BASE}/v1/video/create",
                          headers=HEADERS_RELAY, json=payload, timeout=15)
        # 任何非 404 都说明端点存在
        ok = r.status_code != 404
        log_result("视频", "/v1/video/create", "POST", r.status_code,
                   f"端点存在 (返回 {r.status_code})" if ok else "404 端点不存在", ok)
    except Exception as e:
        log_result("视频", "/v1/video/create", "POST", 0, str(e), False)

    # GET /v1/video/query — 查询端点
    try:
        r = requests.get(f"{API_BASE}/v1/video/query?task_id=test",
                         headers=HEADERS_RELAY, timeout=10)
        ok = r.status_code != 404
        log_result("视频", "/v1/video/query", "GET", r.status_code,
                   f"端点存在 (返回 {r.status_code})" if ok else "404 端点不存在", ok)
    except Exception as e:
        log_result("视频", "/v1/video/query", "GET", 0, str(e), False)

# ============ 8. 认证错误格式验证（文档: error-handling.mdx） ============
def test_error_format():
    section("8. 错误格式验证 (文档: error-handling.mdx)")

    # 无 key 请求应返回 401 + OpenAI 格式错误
    try:
        bad_headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        payload = {"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "hi"}]}
        r = requests.post(f"{API_BASE}/v1/chat/completions",
                          headers=bad_headers, json=payload, timeout=10)
        data = r.json()
        has_error = "error" in data
        error_obj = data.get("error", {})
        has_message = "message" in error_obj
        ok = r.status_code == 401 and has_error and has_message
        log_result("错误格式", "/v1/chat/completions (无key)", "POST", r.status_code,
                   f"error.message: {error_obj.get('message', '?')[:60]}" if ok
                   else f"格式不符预期: {r.text[:80]}", ok)
    except Exception as e:
        log_result("错误格式", "/v1/chat/completions (无key)", "POST", 0, str(e), False)

# ============ 9. 文档示例代码验证（文档: authentication.mdx） ============
def test_doc_example():
    section("9. 文档示例代码验证 (文档: authentication.mdx 中的 cURL 示例)")

    if not API_KEY:
        print("  ⚠️  跳过: 未设置 API_KEY")
        return

    # 模拟文档中 authentication.mdx 的 cURL 示例
    try:
        payload = {
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": "Hi"}]
        }
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        r = requests.post(f"{API_BASE}/v1/chat/completions",
                          headers=headers, json=payload, timeout=30)
        ok = r.status_code == 200
        log_result("示例验证", "authentication.mdx cURL 示例", "POST", r.status_code,
                   "文档示例可正常执行" if ok else f"执行失败: {r.text[:80]}", ok)
    except Exception as e:
        log_result("示例验证", "authentication.mdx cURL 示例", "POST", 0, str(e), False)

# ============ 汇总报告 ============
def print_summary():
    section("验证汇总")
    total = len(results)
    passed = sum(1 for r in results if r["match"])
    failed = sum(1 for r in results if not r["match"])

    print(f"\n  总计: {total} 项测试")
    print(f"  通过: {passed} ✅")
    print(f"  失败: {failed} ❌")
    print(f"  通过率: {passed/total*100:.0f}%" if total > 0 else "  无测试")

    if failed > 0:
        print(f"\n  失败项:")
        for r in results:
            if not r["match"]:
                print(f"    ❌ [{r['method']}] {r['endpoint']} — {r['detail']}")

    # 保存 JSON 报告
    report = {
        "timestamp": datetime.now().isoformat(),
        "api_base": API_BASE,
        "total": total,
        "passed": passed,
        "failed": failed,
        "results": results
    }
    report_path = "docs_api_verify_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"\n  详细报告已保存: {report_path}")

# ============ 主入口 ============
if __name__ == "__main__":
    print(f"Crazyrouter 文档 API 一致性验证")
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"目标: {API_BASE}")
    print(f"API Key: {'已设置' if API_KEY else '未设置 (跳过需认证的测试)'}")
    print(f"Access Token: {'已设置' if ACCESS_TOKEN else '未设置 (跳过管理API测试)'}")

    test_public_endpoints()
    test_chat_api()
    test_image_api()
    test_audio_api()
    test_embeddings_api()
    test_token_management()
    test_video_api()
    test_error_format()
    test_doc_example()
    print_summary()
