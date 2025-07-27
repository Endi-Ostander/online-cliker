[app]
title = ClickerGame
package.name = clickergame
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
orientation = portrait
fullscreen = 0
window = auto

requirements = python3,kivy,requests

android.api = 33
android.minapi = 21
android.ndk = 25.1.8937393
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
android.build_tools_version = 33.0.2
android.archs = armeabi-v7a

android.permissions = INTERNET

log_level = 2

# icon.filename = icon.png
# presplash.filename = splash.png
