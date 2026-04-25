# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with
code in this repository.

## Project Overview

Reference Blender 4.x add-on that embeds the dsviper runtime. Acts as a
starting template for clients building their own Blender extensions on top of
dsviper.

Extracted from `com.digitalsubstrate.viper/dsviper_blender/`. The wheel
distribution mechanism changed: instead of pre-bundling a wheel produced by a
local build, this repo fetches wheels from [PyPI](https://pypi.org/project/dsviper/)
at build time via `fetch_wheels.py`.

## Layout

- `__init__.py` — add-on entry point (`register` / `unregister`), demonstrates
  `import dsviper` works once installed.
- `blender_manifest.toml` — Blender extension metadata. The `wheels = [...]`
  block is rewritten by `fetch_wheels.py` to match downloaded filenames.
- `fetch_wheels.py` — downloads `dsviper` wheels from PyPI for the four
  supported Blender platforms (macos-arm64, macos-x64, windows-x64, linux-x64),
  then rewrites the manifest.
- `wheels/` — created by `fetch_wheels.py`, gitignored.

## Build Commands

```bash
python3 fetch_wheels.py                        # default version, default Python
python3 fetch_wheels.py --version 1.2.8        # pin a release
python3 fetch_wheels.py --python-version 3.12  # for future Blender 5.x

/Applications/Blender.app/Contents/MacOS/Blender --command extension build
```

## Conventions

- Blender platforms ↔ pip platform tags map lives in `fetch_wheels.py:PLATFORMS`.
  Adjust there when Blender bumps its embedded glibc or macOS minimum.
- The manifest's `version` field is bumped manually to track the dsviper
  release the add-on bundles.
- Documentation in **English**.

## Slash Commands and Skills

Inherits skills from the dsviper ecosystem:

- `git-safety` — prevents unauthorized git operations.
- `write-documentation` — ensures markdown is written in English.
