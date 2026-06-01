import subprocess, os

token_file = os.path.expanduser("~/.gh_token")
with open(token_file) as f:
    os.environ["GH_TOKEN"] = f.read().strip()

# Set up git credentials
os.environ["GIT_ASKPASS"] = "echo"
os.environ["GIT_USERNAME"] = "oujiesheng"

gh_path = r"C:\Program Files\GitHub CLI\gh.exe"

# Use gh to push
r = subprocess.run(
    [gh_path, "api", "repos/oujiesheng/bug-bounty"],
    capture_output=True, text=True, timeout=30
)
print("API test:", r.returncode)

# Try git push with GH_TOKEN
r = subprocess.run(
    ["git", "-c", "http.sslVerify=false", "push", "origin", "fix/auth-refresh-verification"],
    capture_output=True, text=True, timeout=30,
    cwd=r"C:\Users\jiesh\auto-bounty\bug-bounty"
)
print("Push stdout:", r.stdout)
print("Push stderr:", r.stderr)
print("Push return:", r.returncode)
