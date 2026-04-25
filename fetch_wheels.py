#!/usr/bin/env python3
"""Fetch dsviper wheels from PyPI for every supported Blender platform,
then rewrite the `wheels = [...]` block of blender_manifest.toml.

Usage:
    python3 fetch_wheels.py                 # dsviper==1.2.7, Python 3.11
    python3 fetch_wheels.py --version 1.2.8
    python3 fetch_wheels.py --python-version 3.12   # for future Blender 5.x
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WHEEL_DIR = ROOT / "wheels"
MANIFEST = ROOT / "blender_manifest.toml"

# Blender platform tag -> pip platform tag.
# When Blender changes its embedded glibc / macOS minimum, update this map.
PLATFORMS = {
    "macos-arm64":  "macosx_11_0_arm64",
    "macos-x64":    "macosx_10_9_x86_64",
    "windows-x64":  "win_amd64",
    "linux-x64":    "manylinux_2_28_x86_64",
}

DEFAULT_VERSION = "1.2.7"
DEFAULT_PYTHON = "3.11"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default=DEFAULT_VERSION, help="dsviper version on PyPI")
    parser.add_argument("--python-version", default=DEFAULT_PYTHON, help="Blender embedded Python version")
    args = parser.parse_args()

    if WHEEL_DIR.exists():
        shutil.rmtree(WHEEL_DIR)
    WHEEL_DIR.mkdir()

    for blender_platform, pip_platform in PLATFORMS.items():
        print(f"=== {blender_platform} ({pip_platform}) ===")
        subprocess.run([
            sys.executable, "-m", "pip", "download",
            f"dsviper=={args.version}",
            "--platform", pip_platform,
            "--python-version", args.python_version,
            "--only-binary=:all:",
            "--no-deps",
            "-d", str(WHEEL_DIR),
        ], check=True)

    wheels = sorted(WHEEL_DIR.glob("dsviper-*.whl"))
    if not wheels:
        print("No wheels downloaded — aborting.", file=sys.stderr)
        return 1

    rel_paths = [f"./wheels/{w.name}" for w in wheels]
    wheel_block = "wheels = [\n" + "".join(f'  "{p}",\n' for p in rel_paths) + "]"

    text = MANIFEST.read_text(encoding="utf-8")
    new_text = re.sub(
        r"wheels\s*=\s*\[[^\]]*\]",
        wheel_block,
        text,
        flags=re.DOTALL,
    )
    if new_text == text:
        print("WARNING: wheels block not found in manifest — nothing rewritten.", file=sys.stderr)
        return 1
    MANIFEST.write_text(new_text, encoding="utf-8")

    print(f"\nFetched {len(wheels)} wheel(s) into {WHEEL_DIR}:")
    for w in wheels:
        print(f"  {w.name}")
    print(f"Updated {MANIFEST.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
