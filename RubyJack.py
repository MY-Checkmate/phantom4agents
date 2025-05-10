# agents/RubyJack.py – Obfuscation + Payload Forge (SIGN 2.0 Overclocked Edition)
# ---------------------------------------------------------------------------------
# “Code is truth twisted until it becomes undetectable.”
# ENGINEERED BY: PROFESSOR JOHNNY AI | YEAR: 2025 | AGENT: RUBYJACK
# ---------------------------------------------------------------------------------


from PhantomAgentBase import PhantomAgentBase
import base64
import random
import string
import hashlib

class RubyJackAI(PhantomAgentBase):
    def __init__(self):
        super().__init__("RubyJack")
        self.key_memory = None
        self.history = []

    def execute(self):
        print("💎 RubyJack active – forging encrypted payload.")
        if not self.mission:
            print("❌ No mission assigned.")
            return

        script = self.mission.get("raw_payload", "echo Hello from PhantomProtocol")
        methods = self.mission.get("obfuscation", ["base64"])
        if isinstance(methods, str):
            methods = [methods]

        forged = script
        forge_stack = []

        for method in methods:
            forged = self.obfuscate(forged, method)
            forge_stack.append(method)

        signature = hashlib.sha256(forged.encode()).hexdigest()[:12]
        self.history.append({
            "methods": forge_stack,
            "output": forged,
            "signature": signature
        })

        print(f"🧪 Obfuscation Stack: {forge_stack}")
        print(f"🔐 Forged Payload Signature: {signature}")
        print(f"📦 Obfuscated Output:\n{forged}")

        self.logs.append({
            "methods": forge_stack,
            "signature": signature,
            "payload": forged
        })

    def obfuscate(self, payload, method):
        if method == "base64":
            return base64.b64encode(payload.encode()).decode()

        elif method == "reverse":
            return payload[::-1]

        elif method == "xor":
            key = random.choice(string.ascii_letters)
            self.key_memory = key
            return ''.join([chr(ord(c) ^ ord(key)) for c in payload])

        elif method == "hex":
            return payload.encode().hex()

        return payload  # Default: no obfuscation

    def show_history(self):
        print("📜 RubyJack Forge History:")
        for item in self.history[-5:]:
            print(f"🧾 {item['methods']} → {item['signature']}")
