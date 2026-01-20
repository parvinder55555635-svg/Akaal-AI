[app]
title = Akaal AI
package.name = akaalai
version = 4.0.0
source.dir = .
source.include_exts = py,png,jpg,kv,bin,gguf
source.include_patterns = models/*

# Required for High-Performance Networking & Security
requirements = python3, kivy==2.3.0, hostpython3, pyjnius, cryptography, certifi

# Android 15 Optimization
android.api = 35
android.minapi = 26
android.sdk = 35
android.ndk = 26b
android.archs = arm64-v8a
android.enable_aapt2 = True

# Sovereign Permissions
android.permissions = INTERNET, RECORD_AUDIO, USE_BIOMETRIC, NEARBY_WIFI_DEVICES, BLUETOOTH_SCAN, BLUETOOTH_CONNECT, ACCESS_FINE_LOCATION
