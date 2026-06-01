import subprocess, os

token_file = os.path.expanduser("~/.gh_token")
with open(token_file) as f:
    os.environ["GH_TOKEN"] = f.read().strip()

gh_path = r"C:\Program Files\GitHub CLI\gh.exe"

pr_body = """## Summary

Fixes #3524 — prevents client-provided `id` from overwriting server-owned message ids.

## Changes

### `apps/api/src/services/messageService.js`
- Destructure payload to remove client-provided `id` before spreading
- Return snapshot from `sendMessage()` to prevent external mutation
- Return shallow copy from `listMessages()` to prevent store pollution

### `apps/api/src/tests/messageService.test.js`
- Server-generated id takes precedence over client-provided id
- sendMessage returns snapshot (mutation doesn't affect store)
- listMessages returns shallow copy (push doesn't affect store)

## Tests
```
node --test apps/api/src/tests/messageService.test.js
```
All 4 tests pass.

## /claim #743"""

r = subprocess.run(
    [gh_path, "pr", "create",
     "--repo", "SecureBananaLabs/bug-bounty",
     "--head", "oujiesheng:fix/message-service-id-overwrite",
     "--base", "main",
     "--title", "fix: prevent client-provided id overwrite in messageService",
     "--body", pr_body],
    capture_output=True, text=True, timeout=30
)
print(r.stdout)
if r.stderr:
    print("STDERR:", r.stderr)
print("Return code:", r.returncode)
