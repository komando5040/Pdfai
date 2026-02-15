[app]
title = PDF Chatbot
package.name = pdfchat
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.1.0,PyPDF2
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
android.accept_sdk_license = True
android.ndk = 25b
android.sdk = 24
android.minapi = 21
android.api = 31
android.arch = arm64-v8a

# Permissions for reading files
android.permissions = android.permission.READ_EXTERNAL_STORAGE, android.permission.WRITE_EXTERNAL_STORAGE
