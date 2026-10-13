#!/usr/bin/env bash
set -euo pipefail
REPO="${1:-/media/ilias/DATA/ilias/AMROD}"
OUT="${2:-/media/ilias/DATA/ilias/amrod_output/paper26_preflight}"
mkdir -p "$OUT"
{
  date -Is
  hostname
  nvidia-smi --query-gpu=index,name,memory.total,memory.free,utilization.gpu --format=csv || true
  df -h "$REPO" "$OUT" || true
  git -C "$REPO" rev-parse HEAD || true
  git -C "$REPO" status --short || true
  find "$REPO/scripts" -maxdepth 1 -type f \( -name '*local*.sh' -o -name '*lt*.sh' \) -printf '%f\n' | sort || true
  find "$REPO/detectron2/configs/Cityscapes" -maxdepth 1 -name '*newsrc*yaml' -printf '%f\n' | sort || true
  grep -R -n -E 'CTCMT_WEIGHT_CTCR|CTCMT_CTCR_WEIGHT_FLOOR|CTCMT_CONFLICT_MODE|STREAM=' "$REPO/scripts" "$REPO/detectron2/configs/Cityscapes" 2>/dev/null | head -120 || true
} > "$OUT/preflight.txt" 2>&1
printf 'Preflight saved: %s/preflight.txt\n' "$OUT"
