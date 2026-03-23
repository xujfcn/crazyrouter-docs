# Crazyrouter Docs Improvement Checklist

Last updated: 2026-03-23

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
- [x] Add production-verified unified capability pages

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

## J. Information Architecture

- [x] Add top-level `核心能力` / `Features` navigation groups to surface tool calling, structured outputs, web search, reasoning, vision, and PDF-related pages without forcing users to choose a protocol first

## K. Unified Capability Pages

- [x] Add `features/tool-calling.mdx` and `en/features/tool-calling.mdx`
- [x] Add `features/structured-outputs.mdx` and `en/features/structured-outputs.mdx`
- [x] Add `features/web-search.mdx` and `en/features/web-search.mdx`
- [x] Add `features/reasoning.mdx` and `en/features/reasoning.mdx`
- [x] Revalidate the four capability pages against Crazyrouter production on `2026-03-22` and narrow claims to reproducible response markers

## L. Reasoning Protocol Cleanup

- [x] Rework `chat/openai/reasoning.mdx` and `en/chat/openai/reasoning.mdx` to separate Chat `reasoning_effort` from Responses-visible reasoning
- [x] Rework `chat/responses/gpt5-thinking.mdx` and `en/chat/responses/gpt5-thinking.mdx` to use production-verified `gpt-5.4` response shapes and stream events
- [x] Rework `reference/thinking.mdx` and `en/reference/thinking.mdx` to document protocol-specific thinking fields instead of outdated cross-protocol assumptions

## M. Protocol Page Refresh

- [x] Rework `chat/openai/web-search.mdx` and `en/chat/openai/web-search.mdx` to document the currently verified Responses-based web-search path
- [x] Rework `chat/anthropic/messages.mdx` and `en/chat/anthropic/messages.mdx` around `claude-sonnet-4-6` and `claude-opus-4-6-thinking`
- [x] Rework `chat/gemini/native.mdx` and `en/chat/gemini/native.mdx` around `gemini-3-pro-preview` and currently verified native capabilities

## N. Overview Page Refresh

- [x] Rework `chat/gemini/openai-compat.mdx` and `en/chat/gemini/openai-compat.mdx` around `gemini-3-pro-preview`
- [x] Rework `chat/responses/overview.mdx` and `en/chat/responses/overview.mdx` around the currently verified `gpt-5.4` Responses behavior
- [x] Rework `chat/openai/overview.mdx` and `en/chat/openai/overview.mdx` to describe the stable Chat Completion object shape without overclaiming optional fields

## O. Model List And Tutorial Refresh

- [x] Rework `chat/openai/models.mdx` and `en/chat/openai/models.mdx` around the `2026-03-23` live `/v1/models` response
- [x] Rework `chat/gemini/openai-models.mdx` and `en/chat/gemini/openai-models.mdx` around the `2026-03-23` live `/v1beta/openai/models` response
- [x] Rework `reference/tutorial.mdx` and `en/reference/tutorial.mdx` into production-verified starter paths instead of generic compatibility claims

## P. Endpoint And Special-Model Refresh

- [x] Rework `chat/openai/special-models.mdx` and `en/chat/openai/special-models.mdx` around the `2026-03-23` live availability check
- [x] Rework `chat/openai/completions.mdx` and `en/chat/openai/completions.mdx` around the current `gpt-5.4` chat object and stream behavior
- [x] Rework `chat/anthropic/overview.mdx` and `en/chat/anthropic/overview.mdx` around `claude-sonnet-4-6` and the current native SSE event sequence

## Q. Remaining Legacy And Multimodal Cleanup

- [x] Rework `chat/gemini/tools.mdx` and `en/chat/gemini/tools.mdx` around the `2026-03-23` live `gemini-3-pro-preview` tool checks
- [x] Rework `chat/gemini/document.mdx` and `en/chat/gemini/document.mdx` around the `2026-03-23` live PDF + schema checks
- [x] Rework `chat/openai/image-creation.mdx` and `en/chat/openai/image-creation.mdx` around the `2026-03-23` observed chat-image response shape and the verified `gpt-image-1` fallback path
- [x] Rework `chat/openai/completions-legacy.mdx` and `en/chat/openai/completions-legacy.mdx` around the `2026-03-23` legacy-model availability result
- [x] Rework `chat/gemini/image-gen.mdx` and `en/chat/gemini/image-gen.mdx` around the `2026-03-23` observed per-model output-shape differences
- [x] Rework `chat/gemini/image-edit.mdx` and `en/chat/gemini/image-edit.mdx` into current availability notes because same-day production retests were unavailable or timed out

## R. Responses And Vision Refresh

- [x] Rework `chat/responses/create.mdx` and `en/chat/responses/create.mdx` around the `2026-03-23` live `gpt-5.4` basic and streaming checks
- [x] Rework `chat/responses/function-calling.mdx` and `en/chat/responses/function-calling.mdx` around the `2026-03-23` live `function_call` output
- [x] Rework `chat/responses/web-search.mdx` and `en/chat/responses/web-search.mdx` around the `2026-03-23` live `web_search_call` output
- [x] Rework `chat/openai/structured-output.mdx` and `en/chat/openai/structured-output.mdx` around the `2026-03-23` live `gpt-5.4` `json_schema` result
- [x] Rework `chat/openai/function-calling.mdx` and `en/chat/openai/function-calling.mdx` around the `2026-03-23` live `gpt-5.4` `tool_calls` result
- [x] Rework `chat/openai/vision.mdx` and `en/chat/openai/vision.mdx` around the `2026-03-23` live `gpt-5.4` data-URL image input
- [x] Rework `chat/anthropic/vision.mdx`, `chat/anthropic/pdf.mdx`, and `chat/anthropic/completions.mdx` plus English counterparts around the `2026-03-23` live `claude-sonnet-4-6` checks
- [x] Rework `chat/gemini/vision.mdx` and `en/chat/gemini/vision.mdx` around the `2026-03-23` live `gemini-3-pro-preview` image-input check

## S. Entry-Page Example Refresh

- [x] Update `quickstart.mdx`, `making-requests.mdx`, and `authentication.mdx` plus English counterparts to use the `2026-03-23` production-verified `gpt-5.4` starter example

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
- 2026-03-22: Added top-level `核心能力` / `Features` groups to `docs.json` so users can find tool calling, structured outputs, web search, reasoning, vision, and PDF capabilities directly from navigation before picking a protocol-specific guide.
- 2026-03-22: Added unified capability hub pages in `features/` and `en/features/` for tool calling, structured outputs, web search, and reasoning so users can start from capability first, then drill into protocol-specific docs.
- 2026-03-22: Revalidated those four capability pages with real requests against `https://crazyrouter.com` and tightened them to the current production behavior: `gpt-5.4` reasoning now uses Responses `reasoning` items as the verified path, Claude tool-calling examples now use a stronger reproducible `/v1/messages` pattern, Claude web search is documented with an explicit prompt that reliably surfaces `remote_web_search`, and Claude structured output remains excluded from strict-success claims because the response shape is not yet stable.
- 2026-03-22: Reworked `chat/openai/reasoning.mdx`, `chat/responses/gpt5-thinking.mdx`, and `reference/thinking.mdx` plus their English counterparts using the same production recheck: Chat Completions reasoning is now documented as a final-answer path rather than a stable visible-trace path, GPT Responses reasoning is documented with the current `reasoning` item shape and verified SSE event names, and the thinking reference now distinguishes Responses `reasoning`, Claude `thinking`, and Gemini `thoughtsTokenCount` instead of mixing them together.
- 2026-03-22: Reworked `chat/openai/web-search.mdx`, `chat/anthropic/messages.mdx`, and `chat/gemini/native.mdx` plus their English counterparts using the same production-first rule: OpenAI web search now documents the verified `gpt-5.4` Responses path instead of the older Chat `web_search` pattern, Claude Messages now uses the current `claude-sonnet-4-6` / `claude-opus-4-6-thinking` models and verified auth/tool/thinking behavior, and Gemini Native now uses `gemini-3-pro-preview` with verified text, SSE streaming, structured outputs, Google Search, and thinking markers.
- 2026-03-22: Reworked `chat/gemini/openai-compat.mdx`, `chat/responses/overview.mdx`, and `chat/openai/overview.mdx` plus their English counterparts so the overview layer no longer lags behind the feature pages: Gemini OpenAI-compatible docs now use the verified `gemini-3-pro-preview` compatibility path, the Responses overview now frames `/v1/responses` around the currently verified `gpt-5.4` reasoning and web-search behavior, and the Chat Completion object page now treats `reasoning_content` as optional rather than a guaranteed cross-model field.
- 2026-03-23: Reworked `chat/openai/models.mdx`, `chat/gemini/openai-models.mdx`, and `reference/tutorial.mdx` plus their English counterparts using a fresh same-day production recheck: `/v1/models` and `/v1beta/openai/models` are now documented with current response shape, auth, and example model IDs such as `gpt-5.4`, `claude-sonnet-4-6`, and `gemini-3-pro-preview`, while the tutorial now focuses on production-verified starter routes instead of broad generic compatibility claims.
- 2026-03-23: Reworked `chat/openai/special-models.mdx`, `chat/openai/completions.mdx`, and `chat/anthropic/overview.mdx` plus their English counterparts using the same-day production check: the special-models page now documents current availability instead of stale success examples because `qwen-mt-turbo` was not present and `deepseek-ocr` was temporarily unavailable, the Chat Completions page now uses the current `gpt-5.4` response and SSE chunk shape, and the Anthropic overview now uses `claude-sonnet-4-6` with the currently observed native SSE event sequence.
- 2026-03-23: Reworked `chat/gemini/tools.mdx`, `chat/gemini/document.mdx`, `chat/openai/image-creation.mdx`, `chat/openai/completions-legacy.mdx`, `chat/gemini/image-gen.mdx`, and `chat/gemini/image-edit.mdx` plus their English counterparts using same-day production checks: Gemini tools are now documented around the verified `gemini-3-pro-preview` tool markers, Gemini document understanding is narrowed to verified PDF and schema-output paths, Chat image creation now documents the currently observed text-wrapped `gpt-4o-image` behavior and points stable automation to `gpt-image-1`, the legacy completions page now records the current `gpt-3.5-turbo-instruct` unavailability result, Gemini image generation now explains the observed per-model output-shape differences, and Gemini image editing is narrowed to a current availability note because all same-day retests failed or timed out.
- 2026-03-23: Reworked `chat/responses/create.mdx`, `chat/responses/function-calling.mdx`, `chat/responses/web-search.mdx`, `chat/openai/structured-output.mdx`, `chat/openai/vision.mdx`, `chat/anthropic/vision.mdx`, `chat/anthropic/pdf.mdx`, `chat/anthropic/completions.mdx`, and `chat/gemini/vision.mdx` plus their English counterparts using same-day production checks: Responses docs now use `gpt-5.4` and current output markers such as `message`, `function_call`, and `web_search_call`; OpenAI structured output and vision now keep only the revalidated `json_schema` and data-URL image-input paths; Claude OpenAI-compatible chat, native vision, and native PDF docs now use `claude-sonnet-4-6` with current response shapes; and Gemini vision is narrowed to the revalidated `gemini-3-pro-preview` image-input path.
- 2026-03-23: Reworked `chat/openai/function-calling.mdx` and `en/chat/openai/function-calling.mdx` using the same-day production check so the Chat Completions tool-calling page now uses `gpt-5.4` and the currently observed `tool_calls` response shape instead of older `gpt-4o` examples.
- 2026-03-23: Updated `quickstart.mdx`, `making-requests.mdx`, and `authentication.mdx` plus their English counterparts so the highest-visibility starter examples now use the same-day production-verified `gpt-5.4` model instead of older `gpt-4o` examples.
