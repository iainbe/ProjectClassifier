#!/bin/bash
# Session-closure enforcement: blocks commits that change toolkit files
# without also staging the audit artefacts.
# Install: cp tools/check_session_closure.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
# Bypass (emergency): git commit --no-verify

STAGED=$(git diff --cached --name-only)
ARTEFACTS="CHANGELOG.md tier2_qa_review.md 10_review_history.csv"

# Do the staged changes include anything OTHER than the 3 artefacts + reports?
CHANGES=$(echo "$STAGED" | grep -v '^CHANGELOG.md$\|^tier2_qa_review.md$\|^10_review_history.csv$\|^sweep_reports/\|^\.git' || true)
if [ -z "$CHANGES" ]; then exit 0; fi

MISSING=""
for a in $ARTEFACTS; do
    echo "$STAGED" | grep -qx "$a" || MISSING="$MISSING $a"
done

if [ -n "$MISSING" ]; then
    echo "SESSION-CLOSURE CHECK FAILED"
    echo "Changed files:$CHANGES" | tr '\n' ' '; echo
    echo "Missing audit artefacts:$MISSING"
    echo "Update CHANGELOG.md, tier2_qa_review.md, 10_review_history.csv and re-stage, or bypass with --no-verify"
    exit 1
fi
exit 0
