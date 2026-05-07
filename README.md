# dsviper-blender

Reference Blender 4.x add-on that embeds the [dsviper](https://pypi.org/project/dsviper/)
runtime. After installation, `import dsviper` works from any Blender Python
script and from the scripting console.

This repo serves as a starting template for clients building their own Blender
extensions on top of dsviper.

## Documentation

Full documentation: https://docs.digitalsubstrate.io/reference-apps/

Part of the [DevKit ecosystem](https://docs.digitalsubstrate.io/).

## Layout

```
dsviper-blender/
├── __init__.py              # Add-on entry point (register / unregister).
├── blender_manifest.toml    # Blender extension metadata. wheels[] is rewritten
│                            #   by fetch_wheels.py — do not edit by hand.
├── fetch_wheels.py          # Downloads dsviper wheels from PyPI for all
│                            #   supported Blender platforms.
├── LICENSE                  # GPL-3.0-or-later (full text).
├── COPYRIGHT                # Project copyright notice and licensing posture.
└── wheels/                  # Created by fetch_wheels.py (gitignored).
```

## Build the add-on

```bash
# 1. Fetch wheels from PyPI for the four supported platforms.
python3 fetch_wheels.py
#
# Optional flags:
#   --version 1.2.8           pin to a specific dsviper release
#   --python-version 3.12     match Blender's embedded Python (5.x will move past 3.11)

# 2. Build the Blender extension.
/Applications/Blender.app/Contents/MacOS/Blender --command extension build
# Produces dsviper_add_on-<version>.zip in the current directory.
```

## Install the add-on in Blender

1. Open Blender, go to **Edit → Preferences → Add-ons**.
2. Click the menu button (top-right of the dialog) and choose **Install from Disk…**.
3. Pick the generated `dsviper_add_on-<version>.zip`.
4. Open the scripting console:

```
>>> import dsviper
>>> dsviper.version()
(1, 2, 7)
```

## Supported platforms

| Blender platform | pip platform tag           |
|------------------|----------------------------|
| `macos-arm64`    | `macosx_11_0_arm64`        |
| `macos-x64`      | `macosx_10_9_x86_64`       |
| `windows-x64`    | `win_amd64`                |
| `linux-x64`      | `manylinux_2_28_x86_64`    |

The mapping lives in `fetch_wheels.py`. Adjust there if Blender bumps its
embedded glibc or macOS minimum.

## Updating after a dsviper release

When a new dsviper version ships on PyPI:

```bash
# Update the manifest version
sed -i '' 's/^version = ".*"/version = "1.2.8"/' blender_manifest.toml

# Re-fetch wheels and rebuild
python3 fetch_wheels.py --version 1.2.8
/Applications/Blender.app/Contents/MacOS/Blender --command extension build
```

## License

GPL-3.0-or-later — full text in [LICENSE](LICENSE), project copyright
notice in [COPYRIGHT](COPYRIGHT). Blender add-ons must be
GPL-compatible (the Blender Python API is GPL-2.0-or-later). dsviper
itself, pulled in at install time, ships under its own license (see
[dsviper on PyPI](https://pypi.org/project/dsviper/)).

## Runtime dependency

At runtime, this Blender add-on bundles the `dsviper` Python package
(downloaded from PyPI by the Blender Extensions packaging step), which
is **proprietary** (PyPI classifier `License :: Other/Proprietary
License`). See
[https://pypi.org/project/dsviper/](https://pypi.org/project/dsviper/)
for the package's licensing posture and contact information.
