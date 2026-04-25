"""dsviper Blender Add-on.

Minimal extension that embeds the dsviper wheel inside a Blender 4.x add-on.
Once installed, `import dsviper` works from any Blender Python script or the
scripting console.

This add-on is a reference template — clients can use it as a starting point
for their own Blender extensions that consume dsviper.
"""

try:
    import dsviper
    print(f"dsviper {dsviper.version()} loaded in Blender")
except ImportError as exc:
    print(f"dsviper failed to load: {exc}")


def register():
    pass


def unregister():
    pass
