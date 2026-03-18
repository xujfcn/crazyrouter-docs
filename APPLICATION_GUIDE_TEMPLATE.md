# Application Guide Template

Last updated: 2026-03-18

Use this template when writing or upgrading any application or integration guide under `crazyrouter-docs/integrations/` or related app-specific pages.

## Required Page Structure

1. Overview
2. Best For
3. Protocol Used
4. Prerequisites
5. Quick Start
6. Recommended Model Setup
7. Token Setup Best Practices
8. Verification Checklist
9. Common Errors and Fixes
10. Performance and Cost Tips
11. FAQ

## Section Requirements

### 1. Overview

- Explain what the application is.
- Explain whether it uses OpenAI-compatible, Anthropic-native, or Gemini-native APIs.
- State the minimum configuration needed to connect to Crazyrouter.

### 2. Best For

Use a short bullet list such as:

- coding assistant
- chat UI
- workflow automation
- team deployment
- local CLI use

### 3. Protocol Used

Always state exactly one of:

- OpenAI-compatible API
- Anthropic Messages API
- Gemini native API

If the application supports multiple modes, explicitly label the recommended one.

### 4. Prerequisites

Include:

- Crazyrouter account
- token or access token type needed
- required model availability
- required local app version if known
- OS assumptions if relevant

### 5. Quick Start

This section must let a user reach first success in under 5 minutes.

Always include:

- exact setting names in the app
- exact base URL
- exact auth variable or field name
- one recommended model
- one simple validation action

### 6. Recommended Model Setup

Use a table like:

| Use case | Recommended model | Why |
|----------|-------------------|-----|
| Fast/cheap | ... | ... |
| Balanced | ... | ... |
| Strongest | ... | ... |

### 7. Token Setup Best Practices

Always cover:

- use a dedicated token for this app
- whether to enable model whitelist
- whether to restrict IPs
- whether to set quota caps
- whether to separate dev/prod tokens

Use a short table:

| Setting | Recommendation | Notes |
|---------|----------------|-------|

### 8. Verification Checklist

Every guide should include a "first success" checklist:

- [ ] app can connect
- [ ] model list loads or model can be selected
- [ ] first request succeeds
- [ ] streaming works if applicable
- [ ] tools / function calling works if applicable
- [ ] logs show successful requests

### 9. Common Errors and Fixes

Use this exact troubleshooting format:

| Symptom | Likely cause | Fix |
|---------|--------------|-----|

Always include common cases where relevant:

- 401 unauthorized
- 403 permission / model not allowed
- 404 wrong base URL
- 429 rate limit / quota issues
- model not found
- streaming not working
- tool calling not working

### 10. Performance and Cost Tips

Keep this practical:

- which model to start with
- when to use cheaper models
- when to split tokens by environment
- when to enable model whitelisting

### 11. FAQ

Include 3 to 6 short Q&A items.

Recommended questions:

- Which base URL should I use?
- Which token should I use?
- Why does model X not appear?
- Why is streaming not working?
- How do I reduce cost?

## Writing Style Rules

- Lead with the fastest working setup.
- Prefer exact UI labels over paraphrases.
- Prefer real env var names over generic wording.
- Avoid documenting routes that are not publicly wired.
- If an endpoint is code-supported but not broadly recommended, label it clearly.
- If behavior differs by Windows/macOS/Linux, separate them explicitly.

## OpenClaw-Specific Additions

OpenClaw pages must additionally include:

- install path and service path
- post-install first-run checklist
- config file locations
- service management commands
- log file locations
- upgrade instructions
- uninstall instructions
- IM integration guidance
- troubleshooting matrix
