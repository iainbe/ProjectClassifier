#!/bin/bash
# run_sweep.sh — wrapper for drive_sweep.py.
# Jobs: (1) run the sweep, (2) make failures loud (marker file + banner in
# SWEEP_LATEST.md + macOS notification), (3) heartbeat file on success,
# (4) drain the remote-trigger queue so launchd QueueDirectories doesn't refire.
set -u

TK="$(cd "$(dirname "$0")/.." && pwd)"
REPORTS="$TK/sweep_reports"
LOG="$REPORTS/sweep.log"
TRIGGER_DIR="/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/sweep_requests"
mkdir -p "$REPORTS" "$TRIGGER_DIR"

{
  echo "===== $(date '+%Y-%m-%d %H:%M:%S') run_sweep start ====="
  /usr/bin/python3 "$TK/tools/drive_sweep.py"
  rc=$?
  echo "===== exit $rc ====="
} >> "$LOG" 2>&1

if [ "$rc" -eq 0 ]; then
  date '+%Y-%m-%d %H:%M:%S' > "$REPORTS/LAST_RUN_OK"
  rm -f "$REPORTS/SWEEP_FAILED.md"
else
  {
    echo "# SWEEP FAILED - $(date '+%Y-%m-%d %H:%M:%S') (exit $rc)"
    echo
    echo "Last 20 log lines:"
    echo
    tail -20 "$LOG"
  } > "$REPORTS/SWEEP_FAILED.md"
  {
    printf '> **SWEEP FAILING - last attempt %s (exit %s). See SWEEP_FAILED.md and sweep.log. Last good report below.**\n\n' "$(date '+%Y-%m-%d %H:%M')" "$rc"
    cat "$REPORTS/SWEEP_LATEST.md" 2>/dev/null
  } > "$REPORTS/SWEEP_LATEST.tmp" && mv "$REPORTS/SWEEP_LATEST.tmp" "$REPORTS/SWEEP_LATEST.md"
  osascript -e "display notification \"Toolkit Drive Sweep FAILED (exit $rc) - see sweep_reports/SWEEP_FAILED.md\" with title \"Toolkit Drive Sweep\" sound name \"Basso\"" 2>/dev/null || true
fi

# Drain the remote-trigger queue (consumed requests) so QueueDirectories doesn't refire.
find "$TRIGGER_DIR" -mindepth 1 -delete 2>/dev/null

exit "$rc"
