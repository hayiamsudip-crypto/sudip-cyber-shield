import os
import json
import socket
import hashlib
import secrets
import string
import platform
from datetime import datetime

from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex

NAVY = get_color_from_hex("#071426")
PANEL = get_color_from_hex("#10243D")
BLUE = get_color_from_hex("#168BFF")
CYAN = get_color_from_hex("#55D6FF")
WHITE = get_color_from_hex("#F3F7FF")
MUTED = get_color_from_hex("#A9BDD5")


class CyberShieldApp(App):
    title = "SUDIP CYBER SHIELD"

    def build(self):
        Window.clearcolor = NAVY
        self.report = {
            "app": "SUDIP CYBER SHIELD",
            "version": "2.1",
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "system": platform.system() or "Android",
            "python_version": platform.python_version(),
            "note": "Local report; no cloud/API used."
        }
        root = BoxLayout(orientation="vertical", padding=dp(14), spacing=dp(10))
        scroll = ScrollView()
        body = BoxLayout(orientation="vertical", spacing=dp(10), size_hint_y=None)
        body.bind(minimum_height=body.setter("height"))

        logo = Image(source=os.path.join(os.path.dirname(__file__), "assets", "icon.png"),
                     size_hint=(1, None), height=dp(150), allow_stretch=True,
                     keep_ratio=True)
        body.add_widget(logo)
        body.add_widget(self.label("SUDIP CYBER SHIELD", 24, WHITE, 52))
        body.add_widget(self.label("LOCAL SECURITY TOOLKIT  •  VERSION 2.1", 12, CYAN, 34))
        body.add_widget(self.label("Local tools only • No cloud server • No API required", 12, MUTED, 42))

        items = [
            ("1. Security Dashboard", self.dashboard),
            ("2. Password Strength Checker", self.password_checker),
            ("3. Generate Strong Password", self.generate_password),
            ("4. File SHA-256 Scanner", self.file_hash),
            ("5. Local Network Analyzer", self.network_info),
            ("6. Security Checklist", self.security_checklist),
            ("7. Save Local Security Report", self.save_report),
            ("8. Ethical Hacking Practice Lab", self.practice_lab),
        ]
        for caption, callback in items:
            btn = Button(text=caption, size_hint_y=None, height=dp(52),
                         background_normal="", background_color=PANEL,
                         color=WHITE, font_size="15sp")
            btn.bind(on_release=lambda _btn, cb=callback: cb())
            body.add_widget(btn)
        body.add_widget(self.label("Use only on devices and files you own or are authorized to test.", 11, MUTED, 46))
        scroll.add_widget(body)
        root.add_widget(scroll)
        return root

    def label(self, text, size=14, color=WHITE, height=40):
        return Label(text=text, font_size=sp(size), color=color, size_hint_y=None,
                     height=dp(height), halign="center", valign="middle",
                     text_size=(Window.width - dp(44), None))

    def popup(self, title, content, height=dp(360)):
        box = BoxLayout(orientation="vertical", padding=dp(12), spacing=dp(10))
        if isinstance(content, str):
            lbl = Label(text=content, color=WHITE, halign="left", valign="top",
                        text_size=(Window.width - dp(80), None))
            box.add_widget(lbl)
        else:
            box.add_widget(content)
        close = Button(text="Close", size_hint_y=None, height=dp(46),
                       background_normal="", background_color=BLUE, color=WHITE)
        box.add_widget(close)
        pop = Popup(title=title, content=box, size_hint=(0.92, None), height=height,
                    separator_color=CYAN, title_color=WHITE)
        close.bind(on_release=pop.dismiss)
        pop.open()
        return pop

    def dashboard(self):
        msg = (
            "LOCAL SECURITY DASHBOARD\n\n"
            f"Operating system: {platform.system() or 'Android'}\n"
            f"Python version: {platform.python_version()}\n"
            f"Device platform: {platform.machine()}\n"
            f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            "API connection: Not used\nCloud server: Not used\n\n"
            "This is not a full malware scan."
        )
        self.report["dashboard_checked_at"] = datetime.now().isoformat(timespec="seconds")
        self.popup("Security Dashboard", msg)

    def password_checker(self):
        box = BoxLayout(orientation="vertical", spacing=dp(10), padding=dp(4))
        entry = TextInput(hint_text="Enter a test password (never your real one)",
                          password=True, multiline=False, size_hint_y=None, height=dp(48))
        box.add_widget(entry)
        result = Label(text="Use a made-up test password.", color=WHITE, halign="left", valign="top")
        box.add_widget(result)
        check = Button(text="Check strength", size_hint_y=None, height=dp(46),
                       background_normal="", background_color=BLUE)
        box.add_widget(check)
        def run_check(*_):
            pw = entry.text
            checks = [
                ("At least 12 characters", len(pw) >= 12),
                ("Uppercase letter", any(c.isupper() for c in pw)),
                ("Lowercase letter", any(c.islower() for c in pw)),
                ("Number", any(c.isdigit() for c in pw)),
                ("Special character", any(not c.isalnum() for c in pw)),
            ]
            score = sum(ok for _, ok in checks)
            lines = [f"[{'OK' if ok else '--'}] {name}" for name, ok in checks]
            result.text = "\n".join(lines) + f"\n\nBasic score: {score}/5\n\nApproximate check only; avoid password reuse."
            self.report["password_checker_last_score"] = score
        check.bind(on_release=run_check)
        self.popup("Password Strength Checker", box, dp(440))

    def generate_password(self):
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+?"
        password = "".join(secrets.choice(alphabet) for _ in range(20))
        box = BoxLayout(orientation="vertical", spacing=dp(12), padding=dp(4))
        box.add_widget(Label(text="Generated password (store privately):", color=WHITE))
        entry = TextInput(text=password, multiline=False, readonly=True, size_hint_y=None, height=dp(52))
        box.add_widget(entry)
        box.add_widget(Label(text="Do not share this password in chat or screenshots.", color=MUTED))
        self.report["password_generated"] = True
        self.popup("Generate Strong Password", box, dp(260))

    def file_hash(self):
        box = BoxLayout(orientation="vertical", spacing=dp(10), padding=dp(4))
        entry = TextInput(hint_text="Full path to a file you own", multiline=False,
                          size_hint_y=None, height=dp(48))
        box.add_widget(entry)
        result = Label(text="Enter a file path, then tap Calculate SHA-256.", color=WHITE,
                       halign="left", valign="top")
        box.add_widget(result)
        btn = Button(text="Calculate SHA-256", size_hint_y=None, height=dp(46),
                     background_normal="", background_color=BLUE)
        box.add_widget(btn)
        def calculate(*_):
            path = entry.text.strip()
            try:
                h = hashlib.sha256()
                size = 0
                with open(path, "rb") as f:
                    for chunk in iter(lambda: f.read(1024 * 1024), b""):
                        size += len(chunk)
                        h.update(chunk)
                result.text = f"File: {os.path.basename(path)}\nSize: {size} bytes\nSHA-256:\n{h.hexdigest()}"
                self.report["last_file_hash"] = {"file": os.path.basename(path), "size": size, "sha256": h.hexdigest()}
            except Exception as exc:
                result.text = f"Could not read file:\n{exc}\n\nOn Android, select an accessible path and grant storage access if required."
        btn.bind(on_release=calculate)
        self.popup("File SHA-256 Scanner", box, dp(390))

    def network_info(self):
        ip = "Unavailable"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("192.0.2.1", 80))
            ip = s.getsockname()[0]
            s.close()
        except OSError:
            pass
        msg = (
            "LOCAL NETWORK INFORMATION\n\n"
            f"Hostname: {socket.gethostname()}\n"
            f"Selected local IP: {ip}\n\n"
            "This selected address may be from a VPN or another interface; it is not guaranteed to be your Wi-Fi IP.\n\n"
            "Wi-Fi details require the Termux:API companion app and are not available in this standalone build.\n\n"
            "SECURITY TIPS\n"
            "• Use WPA2-AES or WPA3 on your router.\n"
            "• Change the router admin password.\n"
            "• Avoid sensitive activity on unknown Wi-Fi.\n\n"
            "This tool does not scan other devices."
        )
        self.report["network_check_at"] = datetime.now().isoformat(timespec="seconds")
        self.popup("Local Network Analyzer", msg, dp(440))

    def security_checklist(self):
        items = [
            "Phone screen lock enabled",
            "Android security updates checked",
            "Unknown apps removed",
            "App permissions reviewed",
            "Two-factor authentication enabled",
            "Important files backed up",
            "Unknown links and APKs avoided",
        ]
        grid = GridLayout(cols=1, spacing=dp(8), size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))
        checks = []
        from kivy.uix.checkbox import CheckBox
        for item in items:
            row = BoxLayout(size_hint_y=None, height=dp(38), spacing=dp(8))
            cb = CheckBox(size_hint_x=None, width=dp(44))
            row.add_widget(cb)
            row.add_widget(Label(text=item, color=WHITE, halign="left"))
            grid.add_widget(row)
            checks.append((item, cb))
        def save_checks(*_):
            self.report["security_checklist"] = [item for item, cb in checks if cb.active]
            self.popup("Checklist Saved", f"Checked {len(self.report['security_checklist'])} of {len(items)} items locally.")
        wrapper = BoxLayout(orientation="vertical", spacing=dp(8))
        scroll = ScrollView()
        scroll.add_widget(grid)
        wrapper.add_widget(scroll)
        save = Button(text="Save checked items", size_hint_y=None, height=dp(44),
                      background_normal="", background_color=BLUE)
        save.bind(on_release=save_checks)
        wrapper.add_widget(save)
        self.popup("Security Checklist", wrapper, dp(440))

    def save_report(self):
        path = os.path.join(self.user_data_dir, "security_report.json")
        self.report["saved_at"] = datetime.now().isoformat(timespec="seconds")
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.report, f, ensure_ascii=False, indent=2)
            self.popup("Local Security Report", f"Report saved successfully:\n\n{path}\n\nNo cloud/API used.")
        except Exception as exc:
            self.popup("Report Error", f"Could not save report:\n{exc}")

    def practice_lab(self):
        msg = (
            "ETHICAL HACKING PRACTICE LAB\n\n"
            "1. HTTPS protects data in transit when correctly configured.\n"
            "2. Never enter passwords through suspicious links.\n"
            "3. pwd shows the current directory in a terminal.\n"
            "4. ls lists files and folders.\n"
            "5. whoami shows the current user.\n\n"
            "Practice only on systems you own or have permission to test."
        )
        self.report["practice_lab_opened"] = True
        self.popup("Ethical Hacking Practice Lab", msg, dp(390))


def sp(value):
    from kivy.metrics import sp as kivy_sp
    return kivy_sp(value)


if __name__ == "__main__":
    CyberShieldApp().run()
