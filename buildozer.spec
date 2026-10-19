[app]
title = SUDIP CYBER SHIELD
package.name = sudipcybershield
package.domain = org.sudipcyber
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,txt
source.exclude_dirs = .git,.github,bin,.buildozer
version = 2.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
icon.filename = assets/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
api = 35
minapi = 23
android.archs = arm64-v8a
android.accept_sdk_license = True
