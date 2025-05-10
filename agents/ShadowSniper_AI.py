# agents/ShadowSniper_AI.py – Full Payload Strike Unit (SIGN 2.0 UPGRADED)
# ------------------------------------------------------------------------------
# “THE FINAL BULLET YOU NEVER HEARD.”
# ENGINEERED BY: PROFESSOR JOHNNY AI | UNIT: SIGN 2.0
# ------------------------------------------------------------------------------
from agents.PhantomAgentBase import PhantomAgentBase
from ops.log_manager import save_log
from datetime import datetime
import hashlib

class ShadowSniperAI(PhantomAgentBase):
    def __init__(self):
        super().__init__("ShadowSniper")
        self.loaded_payload = None
        self.strike_history = []

    def load_payload(self, payload):
        self.loaded_payload = payload
        fingerprint = hashlib.sha256(payload.encode()).hexdigest()[:12]
        self.log(f"🎯 Payload loaded: {payload}")
        self.log(f"🔐 Payload Signature: {fingerprint}")

    def execute_strike(self):
        if not self.loaded_payload:
            msg = "❌ No payload loaded."
            self.log(msg)
            return msg

        ip = self.mission.get("ip")
        if not ip:
            msg = "❌ No target IP in mission."
            self.log(msg)
            return msg

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = f"💥 Payload '{self.loaded_payload}' executed on {ip}"

        strike_record = {
            "ip": ip,
            "payload": self.loaded_payload,
            "signature": hashlib.sha256(self.loaded_payload.encode()).hexdigest()[:12],
            "timestamp": timestamp
        }

        self.strike_history.append(strike_record)
        self.log(result)
        save_log(self.name, "strike", strike_record)
        return result

    def get_strike_history(self, limit=5):
        return self.strike_history[-limit:] if self.strike_history else ["🌀 No strikes logged."]
