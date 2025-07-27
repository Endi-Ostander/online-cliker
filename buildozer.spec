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
android.ndk = 25b
android.archs = armeabi-v7a
android.permissions = INTERNET

# (можно убрать или указать реальные файлы)
icon.filename =
presplash.filename =

# Уровень логов
log_level = 2

# Опционально
# android.packaging = apk
# android.archive_excludes = assets/*.so
