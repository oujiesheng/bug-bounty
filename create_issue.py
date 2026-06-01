import subprocess, os

token_file = os.path.expanduser("~/.gh_token")
with open(token_file) as f:
    os.environ["GH_TOKEN"] = f.read().strip()

gh_path = r"C:\Program Files\GitHub CLI\gh.exe"
r = subprocess.run(
    [gh_path, "issue", "create",
     "--repo", "SecureBananaLabs/bug-bounty",
     "--title", "Message creation should preserve server-owned ids",
     "--body-file", r"C:\Users\jiesh\auto-bounty\bug-bounty\issue_body.md"],
    capture_output=True, text=True, timeout=30
)
print(r.stdout)
if r.stderr:
    print("STDERR:", r.stderr)
print("Return code:", r.returncode)
