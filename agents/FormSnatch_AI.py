# agents/FormSnatch_AI.py – Credential Interceptor & Form Sniffer (🧠 SIGN 2.0 Upgrade)
# -------------------------------------------------------------------------------------
# BUILT TO INTERCEPT. DESIGNED TO UNDERSTAND. ENGINEERED BY: PROFESSOR JOHNNY AI.
# FUNCTION: SNIFF, PROFILE, PRIORITIZE – THEN LOG WITH PURPOSE.
# -------------------------------------------------------------------------------------


from PhantomAgentBase import PhantomAgentBase
import re
import time
import random

class FormSnatchAI(PhantomAgentBase):
    def __init__(self):
        super().__init__("FormSnatch")
        self.field_history = []

    def execute(self):
        print("📝 FormSnatch activated – Credential Surveillance Initialized.")
        if not self.mission:
            print("❌ No mission assigned.")
            return

        page_data = self.mission.get("html_page", "<form><input name='user'><input name='pass'></form>")
        inject_test = self.mission.get("simulate_input", False)

        print("🔍 Scanning HTML for field targets...")
        fields = self.sniff_fields(page_data)
        time.sleep(1)

        if fields:
            print(f"🕵️ Detected Credential Fields: {fields}")
            scored = self.score_fields(fields)
            self.logs.append({
                "fields": fields,
                "priority": scored,
                "source": "HTML",
                "simulated_input": inject_test
            })

            if inject_test:
                self.simulate_input(fields)

            self.field_history.append(fields)
        else:
            print("❌ No form fields detected.")

    def sniff_fields(self, html):
        input_names = re.findall(r'name=["\'](.*?)["\']', html)
        filtered = [f for f in input_names if any(k in f.lower() for k in ["user", "pass", "email", "login"])]
        return filtered if filtered else None

    def score_fields(self, fields):
        priority = {}
        for field in fields:
            if "pass" in field.lower():
                priority[field] = "🟥 HIGH"
            elif "user" in field.lower() or "email" in field.lower():
                priority[field] = "🟧 MEDIUM"
            else:
                priority[field] = "🟨 LOW"
        return priority

    def simulate_input(self, fields):
        print("🧪 Simulating field injection (test mode)...")
        for field in fields:
            fake_value = f"test_{field}_{random.randint(100,999)}"
            print(f"🧬 Injected: {field} → {fake_value}")

    def get_capture_history(self):
        return self.field_history if self.field_history else ["🌀 No history yet."]
