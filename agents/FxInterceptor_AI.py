# agents/FxInterceptor_AI.py – DOM Field Interceptor (Python version of JS logic)

from PhantomAgentBase import PhantomAgentBase
import re

class FxInterceptorAI(PhantomAgentBase):
    def __init__(self):
        super().__init__("FxInterceptor")

    def execute(self):
        print("🕸️ FxInterceptor AI active – scanning input DOM structure.")
        if not self.mission:
            print("❌ No mission assigned.")
            return

        fake_html = self.mission.get(
            "html_input",
            "<input type='text' name='username'><input type='password' name='password'>"
        )

        matches = self.analyze_dom(fake_html)

        if matches:
            print(f"🧠 Intercepted Fields: {matches}")
            self.logs.append({
                "status": "Fields Intercepted",
                "count": len(matches),
                "fields": matches
            })
        else:
            print("✅ No sensitive fields found.")
            self.logs.append({"status": "Clean DOM", "fields": []})

    def analyze_dom(self, html_string):
        print("🔍 Parsing input fields from HTML...")
        input_names = re.findall(r"name=[\"'](.*?)[\"']", html_string, flags=re.IGNORECASE)
        sensitive_keywords = ["user", "pass", "email", "login", "card"]
        filtered = [name for name in input_names if any(key in name.lower() for key in sensitive_keywords)]
        return filtered
