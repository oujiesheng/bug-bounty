#!/bin/bash
GH_TOKEN="$1"
shift
export GH_TOKEN
exec "/c/Program Files/GitHub CLI/gh.exe" "$@"
