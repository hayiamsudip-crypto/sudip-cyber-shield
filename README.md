# SUDIP CYBER SHIELD Android app (v2.2)

This project packages the existing local-only Kivy app as an Android debug APK. It does not use a cloud server or online API.

## Build on GitHub Actions

1. Upload the contents of this folder to the root of a GitHub repository. Include the hidden `.github` folder.
2. Open the repository's **Actions** tab.
3. Choose **Build SUDIP CYBER SHIELD APK** and select **Run workflow**, or push a commit to `main`.
4. When the run succeeds, open the run and download the `sudip-cyber-shield-debug-apk` artifact.
5. Extract that downloaded ZIP to find the APK. Android may ask permission to install apps from that source.

## Build compatibility pins

- GitHub Actions host Python: 3.11
- Buildozer: 1.5.0
- Cython: 0.29.36
- python-for-android: `v2024.01.21` (this release defaults to Android Python 3.11 rather than the newer 3.14 recipe seen in the failed log)
- Android API: 33; NDK: 25b; minimum API: 23; architecture: arm64-v8a

These pins are intended to avoid the Python 3.14 `remote_debugging.c` compilation failure shown in the previous build log. A successful APK is not guaranteed until GitHub Actions completes successfully.

## Notes

- The standalone APK cannot access Termux's `termux-wifi-connectioninfo`; it explains that Wi-Fi details need the Termux:API companion app.
- File SHA-256 requires a path readable by the app. Android scoped storage can restrict access to some folders.
- This is a local toolkit, not a full malware scanner.
- The output is a debug APK, not a Play Store release.
