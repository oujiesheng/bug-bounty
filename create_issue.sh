#!/bin/bash
export GH_TOKEN=*** "/c/Program Files/GitHub CLI/gh.exe" issue create \
  --repo SecureBananaLabs/bug-bounty \
  --title "Message creation should preserve server-owned ids" \
  --body-file /c/Users/jiesh/auto-bounty/bug-bounty/issue_body.md
