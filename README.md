# SUDIP CYBER SHIELD Android app (v2.1)

This is an Android UI version of the local security toolkit. It uses Kivy and performs local-only checks; it does not connect to a cloud server or use an online API.

## Build APK
1. Upload the contents of this folder to a GitHub repository (include the `.github/workflows` folder).
2. Open the repository's **Actions** tab.
3. Select **Build SUDIP CYBER SHIELD APK** and tap **Run workflow** (or push to `main`).
4. When the workflow completes, open the run and download the `sudip-cyber-shield-debug-apk` artifact.
5. Extract the artifact ZIP to get the APK. Android may ask permission to install apps from that source.

## Notes
- The standalone APK cannot access Termux's `termux-wifi-connectioninfo`; it explains that Wi-Fi details need the Termux:API companion app.
- File SHA-256 requires a path readable by the app. Android scoped storage can restrict access to some folders.
- This is a local toolkit, not a full malware scanner.
- The APK produced by this workflow is a debug APK, not a Play Store release.
