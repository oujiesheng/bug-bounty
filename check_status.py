import subprocess, os, json

token_file = os.path.expanduser("~/.gh_token")
with open(token_file) as f:
    os.environ["GH_TOKEN"] = f.read().strip()

gh_path = r"C:\Program Files\GitHub CLI\gh.exe"

# Check PR #3312
r = subprocess.run(
    [gh_path, "pr", "view", "3312",
     "--repo", "SecureBananaLabs/bug-bounty",
     "--json", "state,reviewDecision,comments,updatedAt"],
    capture_output=True, text=True, timeout=30
)
print("=== PR #3312 ===")
print(r.stdout)

# Check PR #3525
r = subprocess.run(
    [gh_path, "pr", "view", "3525",
     "--repo", "SecureBananaLabs/bug-bounty",
     "--json", "state,reviewDecision,comments,updatedAt"],
    capture_output=True, text=True, timeout=30
)
print("=== PR #3525 ===")
print(r.stdout)

# Check notifications
r = subprocess.run(
    [gh_path, "api", "notifications",
     "--jq", '.[] | {repo: .repository.full_name, subject: .subject.title, unread: .unread}'],
    capture_output=True, text=True, timeout=30
)
print("=== 通知 ===")
print(r.stdout)
