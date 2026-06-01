import subprocess, os

token_file = os.path.expanduser("~/.gh_token")
with open(token_file) as f:
    os.environ["GH_TOKEN"] = f.read().strip()

gh_path = r"C:\Program Files\GitHub CLI\gh.exe"

comment = """/attempt #743

Created scoped issue #3524 and submitted PR #3525.

Scope: messageService id overwrite fix
- Server-generated id takes precedence over client-provided id
- Returns snapshots to prevent external mutation
- Returns shallow copies from list functions

Validation:
- `node --test apps/api/src/tests/messageService.test.js` — 4 tests pass
- `git diff --check` — passed

PR: https://github.com/SecureBananaLabs/bug-bounty/pull/3525"""

r = subprocess.run(
    [gh_path, "issue", "comment", "743",
     "--repo", "SecureBananaLabs/bug-bounty",
     "--body", comment],
    capture_output=True, text=True, timeout=30
)
print(r.stdout)
if r.stderr:
    print("STDERR:", r.stderr)
print("Return code:", r.returncode)
