# Crazyrouter Docs Improvement Checklist

Last updated: 2026-03-18

## Rules

- Update this file immediately after each completed item.
- Keep one source of truth for scope, status, and completion notes.
- Mark completed items with `[x]`, in-progress items with `[-]`, pending items with `[ ]`.

## Current Status

- [x] Initialize this checklist and completion log
- [x] Fix factual inconsistencies in existing Mintlify docs
- [x] Add missing docs for already-supported backend endpoints
- [x] Build a standard guide template for application/integration docs
- [x] Expand OpenClaw into a full usage guide
- [x] Upgrade priority application guides
- [x] Upgrade secondary application guides

## A. Fix Existing Doc Inconsistencies

- [x] Remove or correct `POST /api/upload` in `upload.mdx` and `api-endpoint.mdx`
- [x] Replace `GET /api/token/models` with the real supported model-list flow
- [x] Correct `/api/user/self` auth requirements in token/account docs
- [x] Correct Realtime auth docs to remove unsupported `api_key` query usage
- [x] Align token CRUD docs with real request/response fields
- [x] Verify and correct `Sora characters` documentation
- [x] Verify and correct `Replicate native Flux` documentation

## B. Add Docs For Supported But Undocumented Endpoints

- [x] Keep `GET /api/status/page` out of public docs; it is a page-data endpoint behind the user-facing `/status` page
- [x] Keep `GET /api/status/health` out of public docs; it is an ops-facing health endpoint
- [x] Keep `GET /healthz/live` and `GET /healthz/ready` out of public docs; they are deployment probes
- [x] Add Claude token counting doc for `POST /v1/messages/count_tokens`
- [x] Add Gemini compatible model-list doc for `GET /v1beta/openai/models`
- [x] Add video alias doc for `POST /v1/video/generations`
- [x] Add video alias doc for `GET /v1/video/generations/{task_id}`
- [x] Add Ali Bailian video doc

## C. Standardize Application Guide Structure

- [x] Define a common structure for all application guides
- [x] Define a common troubleshooting section format
- [x] Define a common verification checklist for first successful setup
- [x] Define recommended token/model guidance format

## D. OpenClaw Guide Expansion

- [x] Rewrite page structure from install note to full usage guide
- [x] Add post-install first-run verification steps
- [x] Add config file locations and key fields
- [x] Add Crazyrouter token best practices for OpenClaw
- [x] Add model recommendation table by use case
- [x] Add IM integration walkthroughs
- [x] Add service management, restart, and logs section
- [x] Add upgrade guide
- [x] Add uninstall guide
- [x] Add troubleshooting matrix

## E. Priority Application Guides

- [x] Upgrade `integrations/cursor.mdx`
- [x] Upgrade `integrations/claude-code.mdx`
- [x] Upgrade `integrations/codex.mdx`
- [x] Upgrade `integrations/cline.mdx`
- [x] Upgrade `integrations/aider.mdx`

## F. Secondary Application Guides

- [x] Upgrade `integrations/cherry-studio.mdx`
- [x] Upgrade `integrations/lobechat.mdx`
- [x] Upgrade `integrations/nextchat.mdx`
- [x] Upgrade `integrations/dify.mdx`
- [x] Upgrade `integrations/n8n.mdx`
- [ ] Review remaining integration pages and batch-upgrade them

## G. Verification

- [x] Verify key route and auth assumptions against the local Docker test environment on port `4000`
- [x] Tighten n8n setup guidance to reflect version-dependent `Base URL` placement and keep zh/en docs in sync
- [x] Revalidate Cherry Studio guide against official provider docs and keep root-domain guidance as-is
- [x] Revalidate LobeChat guide against official provider docs and keep `/v1` proxy guidance as-is
- [x] Revalidate NextChat setup wording against official docs and the local `4000` status payload
- [x] Revalidate Dify provider guidance against official docs and clarify admin-role requirements
- [x] Add a second-pass Cherry Studio note set for `Manage` / `+` model enablement and full-path `#` edge cases
- [x] Add a second-pass LobeChat note set for `/v1` proxy duplication and self-hosted model pinning
- [x] Add a second-pass NextChat note set for env-only deployments and minimal first-pass validation
- [x] Add a second-pass Dify note set for provider-label variance and one-model-first validation
- [x] Sync `verify_docs_api.py` with the revised public-doc scope for token-management pages

## H. Public-Surface Audit

- [x] Add a public-facing `https://crazyrouter.com/status` link in the introduction pages
- [x] Remove `GET /api/user/self` account-info docs from public docs; keep it as a dashboard/internal user endpoint
- [x] Relabel token-management navigation as API-key / console-facing docs instead of core model-calling APIs
- [x] Add explicit dashboard-auth and non-`sk-xxx` positioning notes to the remaining `/api/token/*` public docs

## I. Deepen Coding Tool Guides

- [x] Expand `integrations/claude-code.mdx` and `en/integrations/claude-code.mdx` with Git / Node install commands, persistent env vars, repo snapshot, and first-run validation
- [x] Further split `integrations/claude-code.mdx` and `en/integrations/claude-code.mdx` into explicit Windows vs macOS install paths, verification commands, and env-var checks
- [x] Expand `integrations/codex.mdx` and `en/integrations/codex.mdx` with Git / Node install commands, `config.toml` writing steps, persistent env vars, repo snapshot, and first-run validation
- [x] Further split `integrations/codex.mdx` and `en/integrations/codex.mdx` into explicit Windows vs macOS install paths, verification commands, and config-file checks
- [x] Expand `integrations/aider.mdx` and `en/integrations/aider.mdx` with Git / Python install commands, official installer steps, persistent env vars, repo snapshot, and first-run validation
- [x] Further refine `integrations/aider.mdx` and `en/integrations/aider.mdx` with explicit Windows vs macOS install paths, command-path verification, and the official `openai/<model>` usage pattern
- [x] Expand `integrations/cline.mdx` and `en/integrations/cline.mdx` with Git / VS Code / extension install steps, repo snapshot guidance, and first-run validation
- [x] Further refine `integrations/cline.mdx` and `en/integrations/cline.mdx` with explicit Windows vs macOS install paths, `code` command verification, UI-based provider setup notes, and VS Code proxy guidance
- [x] Expand `integrations/langchain.mdx` and `en/integrations/langchain.mdx` with Python / JS install steps, env-var persistence, minimal validation, embeddings, and RAG rollout guidance
- [x] Expand `integrations/immersive-translate.mdx` and `en/integrations/immersive-translate.mdx` with full custom-URL setup, model guidance, rate-limit notes, and first-pass translation validation
- [x] Expand `integrations/coze.mdx` and `en/integrations/coze.mdx` with public-safe HTTP plugin / workflow guidance, enterprise custom-model boundary notes, staged validation, and troubleshooting
- [x] Expand `integrations/chatbox.mdx` and `en/integrations/chatbox.mdx` with official-provider-aligned host/path guidance, model rollout order, knowledge-base notes, and troubleshooting
- [x] Expand `integrations/zotero.mdx` and `en/integrations/zotero.mdx` with plugin-selection guidance, custom-endpoint boundary notes, staged academic validation, and troubleshooting

## Completion Log

- 2026-03-18: Created `crazyrouter-docs/DOCS_IMPROVEMENT_CHECKLIST.md` and initialized the tracking workflow.
- 2026-03-18: Corrected unsupported public upload documentation in `upload.mdx`, `en/upload.mdx`, `api-endpoint.mdx`, and `en/api-endpoint.mdx`.
- 2026-03-18: Rewrote token model-list docs to use the real public endpoint `GET /v1/models` in `token-management/models.mdx` and `en/token-management/models.mdx`.
- 2026-03-18: Corrected `/api/user/self` auth guidance in `token-management/account.mdx` and `en/token-management/account.mdx`.
- 2026-03-18: Corrected Realtime authentication guidance in `audio/realtime.mdx` and `en/audio/realtime.mdx`.
- 2026-03-18: Aligned token CRUD docs with current request/response fields in `token-management/create|list|update|search.mdx` and their English counterparts.
- 2026-03-18: Removed unsupported public-route claims from `video/sora.mdx`, `en/video/sora.mdx`, `images/flux.mdx`, and `en/images/flux.mdx`.
- 2026-03-18: Added `crazyrouter-docs/APPLICATION_GUIDE_TEMPLATE.md` to standardize structure, troubleshooting, verification, and token/model guidance for application docs.
- 2026-03-18: Rewrote `openclaw-deploy.mdx` and `en/openclaw-deploy.mdx` into full usage guides covering setup, verification, config, model selection, IM integration, operations, upgrades, uninstall, and troubleshooting.
- 2026-03-18: Upgraded `integrations/cursor.mdx` and `en/integrations/cursor.mdx` into full setup guides with BYOK limitations, token strategy, model recommendations, verification, and troubleshooting.
- 2026-03-18: Upgraded `integrations/claude-code.mdx` and `en/integrations/claude-code.mdx` into full setup guides covering Anthropic-native setup, token strategy, model recommendations, validation, and troubleshooting.
- 2026-03-18: Upgraded `integrations/codex.mdx` and `en/integrations/codex.mdx` into full setup guides covering custom provider setup, Responses API routing, token strategy, validation, and troubleshooting.
- 2026-03-18: Upgraded `integrations/cline.mdx` and `en/integrations/cline.mdx` into full setup guides covering OpenAI Compatible provider setup, agent permission strategy, validation, and troubleshooting.
- 2026-03-18: Upgraded `integrations/aider.mdx` and `en/integrations/aider.mdx` into full setup guides covering OpenAI-compatible setup, config file strategy, model recommendations, validation, and troubleshooting.
- 2026-03-18: Upgraded `integrations/cherry-studio.mdx` and `en/integrations/cherry-studio.mdx` into full desktop usage guides covering provider setup, model management, MCP rollout order, validation, and troubleshooting.
- 2026-03-18: Upgraded `integrations/lobechat.mdx` and `en/integrations/lobechat.mdx` into full setup guides covering OpenAI proxy setup, self-host deployment defaults, model strategy, validation, and troubleshooting.
- 2026-03-18: Upgraded `integrations/nextchat.mdx` and `en/integrations/nextchat.mdx` into full setup guides covering root-domain base URL usage, self-host environment variables, model rollout, validation, and troubleshooting.
- 2026-03-18: Upgraded `integrations/dify.mdx` and `en/integrations/dify.mdx` into full platform guides covering model-provider setup, chat-first rollout, embedding strategy, environment isolation, validation, and troubleshooting.
- 2026-03-18: Upgraded `integrations/n8n.mdx` and `en/integrations/n8n.mdx` into full automation guides covering OpenAI credentials, minimal workflows, AI Agent rollout, HTTP Request fallback, validation, and troubleshooting.
- 2026-03-18: Verified key documented routes and auth patterns against the local Docker test environment on `http://127.0.0.1:4000`, including `/healthz/live`, `/api/status/health`, `/api/status/page`, `GET /v1/models`, `POST /v1/messages/count_tokens`, `GET /v1beta/openai/models`, `POST /v1/responses`, and video task routes.
- 2026-03-18: Synced `en/integrations/n8n.mdx` with the updated Chinese guide and clarified that `Base URL` may be credential-level or node-level depending on n8n version, with node-level setup preferred for first-pass Crazyrouter validation.
- 2026-03-18: Rechecked `integrations/cherry-studio.mdx` and `en/integrations/cherry-studio.mdx` against Cherry Studio's current provider docs; kept the root-domain `API URL` guidance as-is because Cherry Studio documents root-address entry for OpenAI-compatible upstreams and model management via `Manage` or manual add.
- 2026-03-18: Rechecked `integrations/lobechat.mdx` and `en/integrations/lobechat.mdx` against current LobeChat provider docs; kept the `/v1` proxy guidance as-is because LobeChat documents `OPENAI_PROXY_URL` as the OpenAI request base URL and shows `/v1`-style defaults/examples.
- 2026-03-18: Tightened `integrations/nextchat.mdx` and `en/integrations/nextchat.mdx` to justify root-domain `BASE_URL` guidance with the official NextChat docs pattern plus the local `http://127.0.0.1:4000/api/status` `server_address`, instead of relying on an implicit `/v1` implementation claim.
- 2026-03-18: Tightened `integrations/dify.mdx` and `en/integrations/dify.mdx` to align with official Dify provider docs, clarifying that Crazyrouter should be entered as a custom OpenAI-compatible upstream via `API Base URL` and that `Model Provider` configuration typically requires workspace-admin or owner permissions.
- 2026-03-18: Added a second-pass practical note set to `integrations/cherry-studio.mdx` and `en/integrations/cherry-studio.mdx`, covering root-URL auto-path behavior, when the special trailing-`#` mode is actually needed, and the common `Manage`-list vs enabled-model-list confusion during first validation.
- 2026-03-18: Added a second-pass practical note set to `integrations/lobechat.mdx` and `en/integrations/lobechat.mdx`, covering `/v1` proxy reasoning, duplicate-suffix failures behind custom reverse proxies, and a tighter self-hosted starter model list via `OPENAI_MODEL_LIST`.
- 2026-03-18: Added a second-pass practical note set to `integrations/nextchat.mdx` and `en/integrations/nextchat.mdx`, clarifying that some deployments expose settings only through env vars and that the minimal first-pass validation path should stay `API Key` + root `BASE_URL` + `gpt-4.1`.
- 2026-03-18: Added a second-pass practical note set to `integrations/dify.mdx` and `en/integrations/dify.mdx`, clarifying provider-label / plugin variance across Dify versions and reinforcing the one-provider, one-LLM, one-chat-app validation sequence before adding embeddings or rerank.
- 2026-03-18: Synced `verify_docs_api.py` with the revised public-doc scope by removing the withdrawn `GET /api/user/self` doc check, relabeling the token-management verification section as console/API-key scope, and fixing token-list count extraction to match the current paginated response shape.
- 2026-03-18: Added status-page docs in `reference/status-page.mdx` and `en/reference/status-page.mdx`, documenting the public `GET /api/status/page` aggregate payload for system state, traffic, response-time trends, and service health; later withdrawn from public docs after deciding `/status` is the correct user-facing surface.
- 2026-03-18: Added health-check docs in `reference/health-check.mdx` and `en/reference/health-check.mdx`, documenting the public `GET /api/status/health` endpoint and how it differs from readiness probes; later withdrawn from public docs because it is ops-facing.
- 2026-03-18: Added infrastructure probe docs in `reference/infra-probes.mdx` and `en/reference/infra-probes.mdx`, covering `GET /healthz/live` and `GET /healthz/ready` for liveness/readiness probing; later withdrawn from public docs because they are deployment probes.
- 2026-03-18: Added Claude token-counting docs in `chat/anthropic/count-tokens.mdx` and `en/chat/anthropic/count-tokens.mdx`, documenting `POST /v1/messages/count_tokens`, its auth pattern, estimate semantics, and image/file warning behavior.
- 2026-03-18: Added Gemini-compatible model-list docs in `chat/gemini/openai-models.mdx` and `en/chat/gemini/openai-models.mdx`, documenting `GET /v1beta/openai/models` and its Gemini-style auth with OpenAI-style list semantics.
- 2026-03-18: Added video alias creation docs in `video/openai-video-alias-create.mdx` and `en/video/openai-video-alias-create.mdx`, documenting `POST /v1/video/generations` as a compatibility route and noting the verified local business-error behavior when a model is unavailable.
- 2026-03-18: Added video alias query docs in `video/openai-video-alias-query.mdx` and `en/video/openai-video-alias-query.mdx`, documenting `GET /v1/video/generations/{task_id}` and the verified `task_not_exist` behavior for missing tasks.
- 2026-03-18: Added Ali Bailian video docs in `video/alibailian.mdx` and `en/video/alibailian.mdx`, documenting `/alibailian/api/v1/services/aigc/video-generation/video-synthesis` and `/alibailian/api/v1/tasks/{task_id}` with request/response examples and verified local route behavior.
- 2026-03-18: Updated `docs.json` navigation to surface the new operational health, Claude token counting, Gemini-compatible model-list, video alias, and Ali Bailian pages in both Chinese and English.
- 2026-03-18: With product-direction clarification that `https://crazyrouter.com/status` is the user-facing surface, removed the public docs pages for `GET /api/status/page`, `GET /api/status/health`, `GET /healthz/live`, and `GET /healthz/ready`; these routes are now treated as internal page-data / ops / probe endpoints rather than public user documentation.
- 2026-03-18: Added a public-facing `https://crazyrouter.com/status` link to `introduction.mdx` and `en/introduction.mdx` so users are sent to the real service-status surface instead of internal status APIs.
- 2026-03-18: Removed `token-management/account.mdx` and `en/token-management/account.mdx` from public docs because `GET /api/user/self` is a dashboard/internal user endpoint with role, referral, and settings payloads, not a main public integration API.
- 2026-03-18: Renamed the token section in `docs.json` to `API Key & 控制台管理` / `API Key & Console Management` to clarify that this area is for API-key scope checks and console-side token automation, not the main model-calling API surface.
- 2026-03-18: Added explicit dashboard-auth notes to `token-management/create|list|update|delete|search.mdx` and their English counterparts, and filled in missing auth sections on the update/delete/search pages so users do not mistake these console APIs for normal `sk-xxx` model endpoints.
- 2026-03-18: Deepened `integrations/claude-code.mdx` and `en/integrations/claude-code.mdx` from quick setup pages into fuller operational guides covering Git installation, Node installation, Claude Code installation, temporary and persistent env vars, repo snapshotting, and staged first-run validation.
- 2026-03-18: Further refined `integrations/claude-code.mdx` and `en/integrations/claude-code.mdx` with explicit Windows vs macOS install paths, OS-specific `claude` verification commands like `where.exe` / `which`, clearer temporary-variable echo checks, and PowerShell-vs-Git-Bash guidance for first-time Windows setup.
- 2026-03-18: Deepened `integrations/codex.mdx` and `en/integrations/codex.mdx` with full Git / Node prerequisites, `OPENAI_API_KEY` persistence, exact `~/.codex/config.toml` writing steps, repo snapshot guidance, and safer first-run validation order.
- 2026-03-18: Further refined `integrations/codex.mdx` and `en/integrations/codex.mdx` with explicit Windows vs macOS install paths, OS-specific `codex` installation commands, verification commands like `where.exe` / `which`, and config-file inspection steps after writing `~/.codex/config.toml`.
- 2026-03-18: Deepened `integrations/aider.mdx` and `en/integrations/aider.mdx` with Git / Python prerequisites, the official Aider installer flow, env-var persistence, optional `~/.aider.conf.yml`, repo snapshot guidance, and staged first validation.
- 2026-03-18: Deepened `integrations/cline.mdx` and `en/integrations/cline.mdx` with Git setup, VS Code installation, Cline extension installation, repo snapshot guidance, and a safer read-only-first validation sequence.
- 2026-03-18: Further refined `integrations/aider.mdx` and `en/integrations/aider.mdx` with explicit Windows vs macOS install paths, `where.exe` / `which` verification, safer persistent env-var checks, and the official Aider `openai/<model>` naming pattern for Crazyrouter's OpenAI-compatible route.
- 2026-03-18: Further refined `integrations/cline.mdx` and `en/integrations/cline.mdx` with explicit Windows vs macOS install paths, optional `code` command verification, clearer UI-only provider setup guidance, and a note that Cline reuses VS Code proxy settings on restricted networks.
- 2026-03-18: Expanded `integrations/langchain.mdx` and `en/integrations/langchain.mdx` into fuller framework guides covering Python and JavaScript package installation, persistent `OPENAI_API_KEY` handling, minimal chat validation, embeddings, prompt chains, RAG rollout order, and LangChain-specific troubleshooting for Crazyrouter.
- 2026-03-18: Expanded `integrations/immersive-translate.mdx` and `en/integrations/immersive-translate.mdx` with the official full-path custom OpenAI URL pattern, safer first-pass model choices, request-rate cautions, and a clearer small-text-first validation flow for Crazyrouter-based translation.
- 2026-03-18: Expanded `integrations/coze.mdx` and `en/integrations/coze.mdx` to reposition the public guide around Coze API plugins and workflow HTTP request nodes, explicitly avoid overclaiming enterprise custom-model support, and add staged validation, token-scope guidance, and troubleshooting.
- 2026-03-18: Expanded `integrations/chatbox.mdx` and `en/integrations/chatbox.mdx` into fuller desktop guides covering provider selection, root-host plus default-path setup, staged model rollout, knowledge-base rollout order, token hygiene, and practical ChatBox troubleshooting for Crazyrouter.
- 2026-03-18: Expanded `integrations/zotero.mdx` and `en/integrations/zotero.mdx` into fuller research-workflow guides that distinguish between plugins with custom OpenAI-compatible endpoint support and plugins that only accept official OpenAI keys, while adding Zotero desktop install notes, staged single-paper validation, token hygiene, and troubleshooting.
