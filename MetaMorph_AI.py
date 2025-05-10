# agents/MetaMorph_AI.py – Recon + Adaptive via Shared AI Brain (SIGN 2.0 Upgrade)
# --------------------------------------------------------------------------------
# METAMORPH IS NO LONGER JUST A SCANNER. IT IS A SHAPE THAT THINKS.
# ENGINEERED BY: PROFESSOR JOHNNY AI | YEAR: 2025 | LEGION: SIGN 2.0
# --------------------------------------------------------------------------------

from agents.PhantomAgentBase import PhantomAgentBase
from ops.log_manager import save_log
from datetime import datetime
import random

class MetaMorphAI(PhantomAgentBase):
    def __init__(self):
        super().__init__("MetaMorph")
        self.adaptation_level = 0
        self.current_env = {}
        self.memory_log = []
        self.traits = ["Scanner", "Adapter", "Shape-Shifter"]

    def scan_environment(self, data):
        self.current_env = data
        self.adaptation_level += 1

        self.log(f"📡 Scanned environment: {data}")
        self.log(f"🧬 Adaptation level now: {self.adaptation_level}")

        snapshot = {
            "scan_id": f"S-{random.randint(1000,9999)}",
            "env": data,
            "level": self.adaptation_level,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.memory_log.append(snapshot)

        save_log(self.name, "scan_env", snapshot)

        if self.adaptation_level % 3 == 0:
            self.log("🔁 Threshold reached – adapting trait set.")
            self.trigger_adaptation()

    def trigger_adaptation(self):
        # Dynamically add/change traits
        new_trait = random.choice(["Disguise", "NoiseMask", "StealthBurst", "AutoScout"])
        if new_trait not in self.traits:
            self.traits.append(new_trait)
            self.log(f"🧠 Trait evolved: {new_trait}")
        else:
            self.log(f"↩️ Trait reinforced: {new_trait}")

    def report_status(self):
        status = {
            "current_env": self.current_env,
            "adaptation_level": self.adaptation_level,
            "active_traits": self.traits,
            "snapshots": len(self.memory_log)
        }
        self.log(f"📋 Status Report: {status}")
        return status

    def get_memory_log(self):
        return self.memory_log if self.memory_log else ["🌀 No scans yet."]
