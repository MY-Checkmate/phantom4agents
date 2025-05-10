# agents/SkimScan.py – Beast Mode ATM Skimmer + Fake PIN UI (SIGN 2.0 Finalized)
# ------------------------------------------------------------------------------
# INTERFACE DECEPTION ENGINEERED BY: PROFESSOR JOHNNY AI
# THIS AGENT REDEFINES HUMAN-CODE INTERACTION WITH A DIGITAL MASK.
# ------------------------------------------------------------------------------

from PhantomAgentBase import PhantomAgentBase
import random
import string
import time
import hashlib

class SkimScanAI(PhantomAgentBase):
    def __init__(self):
        super().__init__("SkimScan")

    def execute(self):
        print("💳 SkimScan BEAST MODE initiated – target interface scanning.")
        if not self.mission:
            print("❌ No mission assigned.")
            return

        markup = self.mission.get("ui_markup", "<input type='password' name='pin'>")
        mode = self.mission.get("overlay_mode", "fakepad")
        fake_inputs = self.mission.get("input_variants", 3)
        delay = self.mission.get("inject_delay", 2)

        print(f"⏱️ Injection delay: {delay}s | Mode: {mode} | Variants: {fake_inputs}")
        time.sleep(delay)

        if "pin" in markup.lower():
            overlay = self.build_overlay(markup, mode, fake_inputs)
            sig = hashlib.sha256(overlay.encode()).hexdigest()[:12]
            print(f"🔐 UI injected. Signature: {sig}")
            print("🧪 Payload:\n" + overlay)
            self.logs.append({
                "status": "overlay injected",
                "mode": mode,
                "sig": sig,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })
        else:
            print("❌ No PIN-related input found.")

    def build_overlay(self, html, mode, variants):
        overlays = []
        if mode == "clone":
            for _ in range(variants):
                modified = html.replace("input", f"input class='skim-{random.randint(100,999)}'")
                overlays.append(modified)
        elif mode == "fakepad":
            pad = "<div class='phantom-pinpad'>"
            for i in range(10):
                pad += f"<button>{i}</button>"
            pad += "</div>"
            overlays.append(pad)
        else:
            overlays.append("<!-- Unrecognized overlay mode -->")

        return "\n".join(overlays)
