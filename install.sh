#!/usr/bin/env sh
# macOS / Linux entry point; the Windows equivalents are install-codex.cmd and install-dsh.cmd.
set -eu
cd "$(dirname "$0")"
if command -v python3 >/dev/null 2>&1; then
  exec python3 install.py "$@"
fi
exec python install.py "$@"