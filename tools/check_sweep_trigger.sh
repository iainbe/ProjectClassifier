#!/bin/bash
# check_sweep_trigger.sh — polls the remote-trigger queue.
# launchd QueueDirectories does not fire reliably on Google Drive File Provider
# mounts, so this script runs on a short StartInterval and invokes the real
# sweep when a trigger file has synced in. Exits silently when queue is empty.
set -u

TK="$(cd "$(dirname "$0")/.." && pwd)"
TRIGGER_DIR="/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/sweep_requests"

[ -d "$TRIGGER_DIR" ] || mkdir -p "$TRIGGER_DIR"

if [ -n "$(find "$TRIGGER_DIR" -mindepth 1 -maxdepth 1 -print -quit 2>/dev/null)" ]; then
  exec /bin/bash "$TK/tools/run_sweep.sh"
fi
exit 0
