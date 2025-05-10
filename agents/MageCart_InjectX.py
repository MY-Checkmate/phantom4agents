# agents/MageCart_InjectX.py – Supply Chain Skimmer + Checkout Interceptor (SIGN 2.0)
# ------------------------------------------------------------------------------------
# ENGINEERED BY: PROFESSOR JOHNNY AI | YEAR: 2025
# FORMS DON’T JUST GET INTERCEPTED — THEY GET GHOSTED.
# THIS AGENT INJECTS, OBFUSCATES, AND LOGS SUPPLY CHAIN INTRUSIONS.
# ------------------------------------------------------------------------------------


from PhantomAgentBase import PhantomAgentBase
import re
import random
import base64

class MageCartInjectX(PhantomAgentBase):
    def __init__(self):
        super().__init__("MageCart_InjectX")
        self.injection_log = []

    def execute(self):
        print("🛒 MageCart Inject-X engaged – targeting checkout chains.")
        if not self.mission:
            print("❌ No mission assigned.")
            return

        page = self.mission.get("checkout_html", "<input type='text' name='cc'>")
        inject_mode = self.mission.get("inject_mode", "clone")
        stealth = self.mission.get("stealth_mode", True)

        if "<input" in page and any(tag in page for tag in ["name='cc'", "name='card'", "type='password'"]):
            payload_js = self.generate_js(inject_mode, stealth)
            print("📦 Vector confirmed – executing JS injection.")
            print(f"💉 Injected JS:\n{payload_js}")
            self.injection_log.append({
                "mode": inject_mode,
                "stealth": stealth,
                "status": "simulated",
                "payload": payload_js
            })
            self.logs.append(self.injection_log[-1])
        else:
            print("❌ No valid checkout form detected. Injection aborted.")

    def generate_js(self, mode, stealth=True):
        if mode == "clone":
            js = "document.body.innerHTML += '<script>alert(\"Fake Cart Loaded\")</script>';"
        elif mode == "overlay":
            js = "document.getElementById('checkout').innerHTML = '🔒 Phantom Secure Checkout Active';"
        else:
            js = "// Invalid mode – no JS generated"

        if stealth:
            obfuscated = base64.b64encode(js.encode()).decode()
            return f"eval(atob('{obfuscated}'))  // Stealth Payload"
        return js

    def injection_digest(self):
        return self.injection_log if self.injection_log else ["🌀 No injections logged."]
