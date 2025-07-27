[app]
# (обязательные параметры)
title = ClickerGame
package.name = clickergame
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
orientation = portrait

# Зависимости Python (твой код использует kivy и requests)
requirements = python3,kivy,requests

# Минимальная версия API Android
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b
android.arch = armeabi-v7a

# Настройки иконки (можно оставить пустым или указать свой файл)
icon.filename = 

# Настройки пакета (если нужно, можно добавить)
presplash.filename = 

# (опционально) версия python, если нужно
# python.version = 3.10.5

# Дополнительно (опционально)
fullscreen = 0
window = auto

# (если нужен лог)
log_level = 2

# (если нужно, чтобы разрешить интернет)
android.permissions = INTERNET

# Путь к главному файлу (если не main.py)
# source.include_patterns =

# (опционально) сжатие
# android.packaging = apk

# (опционально) сжимать assets
# android.archive_excludes = assets/*.so
