#!/usr/bin/env bash
# Phase 0 shared environment. Source this before any Phase 0 work.
# No secrets here — keys live in /data/AI_Video/.secrets/AI_Doctor_Theater/*.env (0600),
# injected only via `set -a; . <file>; set +a` when needed. Never via argv.
ROOT=/data/AI_Video/AI_Doctor_Theater
SEC=/data/AI_Video/.secrets/AI_Doctor_Theater
TOOLS=/data/AI_Video/.tools
export PATH="$TOOLS/node22/bin:$TOOLS/bin:$PATH"

# Keep caches and temp files off the 89%-full root partition (supervisor P0-f)
XDG_CACHE_HOME=/data/AI_Video/.cache
TMPDIR=/data/AI_Video/.tmp
npm_config_cache=/data/AI_Video/.cache/npm
PIP_CACHE_DIR=/data/AI_Video/.cache/pip
UV_CACHE_DIR=/data/AI_Video/.cache/uv
export XDG_CACHE_HOME TMPDIR npm_config_cache PIP_CACHE_DIR UV_CACHE_DIR
mkdir -p "$XDG_CACHE_HOME" "$TMPDIR" "$npm_config_cache" "$PIP_CACHE_DIR" "$UV_CACHE_DIR"

# Strict defaults for a multi-user host
umask 077

# lumenx runtime dirs on /data (supervisor condition 3); no OSS, local files only (N6)
LUMENX_DATA_DIR=$ROOT/data/lumenx/home
LUMENX_LOG_DIR=$ROOT/data/lumenx/logs
OSS_ENABLE=false
export LUMENX_DATA_DIR LUMENX_LOG_DIR OSS_ENABLE
mkdir -p "$LUMENX_DATA_DIR" "$LUMENX_LOG_DIR"

# Local addresses must bypass any outbound proxy (clash on this host)
NO_PROXY='*.aliyuncs.com,localhost,127.0.0.1'
no_proxy="$NO_PROXY"
export NO_PROXY no_proxy

# Registry mirrors reachable from this network (comment out if not needed)
export NPM_CONFIG_REGISTRY=https://registry.npmmirror.com
export PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
