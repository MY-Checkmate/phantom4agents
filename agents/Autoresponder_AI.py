# agents/AutoResponder_AI.py – Reflexive Threat Response Sentinel (SIGN 2.0 Upgrade)
# ---------------------------------------------------------------------------------
# AUTO-INTELLIGENT LISTENER FOR LIVE THREATS.
# RESPONDS TO KEYWORDS, FILE SIGNALS, & DYNAMIC ATTACKS.
# POWERED BY: PROFESSOR JOHNNY AI | YEAR 2025
# ---------------------------------------------------------------------------------

import time
from agents.ShadowSniper_AI import ShadowSniperAI
from agents.GhostScroll_AI import GhostScrollAI

class AutoResponderAI:
    def __init__(self, log_path="ghost_ops.log"):
        self.log_path = log_path
        self.sniper = ShadowSniperAI()
        self.ghost = GhostScrollAI()
        self.trigger_words = {
            "threat": self.deploy_threat_response,
            "fire": self.auto_fire_protocol
        }
        self.last_line = ""
        self.active = True

    def watch(self):
        self.ghost.record_event("👁️ AutoResponder AI Activated. Listening for triggers...")
        while self.active:
            try:
                with open(self.log_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    if lines:
                        new_line = lines[-1].strip()
                        if new_line != self.last_line:
                            self.last_line = new_line
                            self.process_line(new_line)
            except Exception as e:
                self.ghost.record_event(f"⚠️ AutoResponder Error: {e}")
            time.sleep(2)

    def process_line(self, line):
        for trigger, action in self.trigger_words.items():
            if trigger in line.lower():
                self.ghost.record_event(f"🔔 Trigger word detected: '{trigger}' in → {line}")
                action(line)

    def deploy_threat_response(self, message):
        self.ghost.record_event(f"🛡️ Reactive Mode: Threat Response on → {message}")
        self.sniper.load_payload("defend_threat.bin")
        result = self.sniper.execute_strike()
        self.ghost.record_event(f"🎯 Auto Threat Counter: {result}")

    def auto_fire_protocol(self, message):
        self.ghost.record_event(f"🔥 Emergency FIRE Triggered → {message}")
        self.sniper.load_payload("auto_fire_payload.exe")
        result = self.sniper.execute_strike()
        self.ghost.record_event(f"💥 Auto FIRE Response: {result}")

    def terminate(self):
        self.active = False
        self.ghost.record_event("🛑 AutoResponder AI shutting down...")
