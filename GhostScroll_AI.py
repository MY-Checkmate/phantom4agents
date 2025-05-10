# agents/GhostScroll_AI.py – Memory & Event Logger (SIGN 2.0 Upgrade)
# -------------------------------------------------------------------------------
# GHOSTSCROLL IS THE MEMORY CORE OF SIGN 2.0
# A LOGGER THAT DOESN'T JUST RECORD – IT REMEMBERS.
# ENGINEERED BY: PROFESSOR JOHNNY AI | YEAR: 2025
# -------------------------------------------------------------------------------

from datetime import datetime
from ops.log_manager import save_log
import json

class GhostScrollAI:
    def __init__(self, log_path="ghost_ops.log"):
        self.log_path = log_path
        self.memory = []
        self.index = 0

    def record_event(self, message, tag="info"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.index += 1
        entry = {
            "index": self.index,
            "timestamp": timestamp,
            "tag": tag,
            "message": message
        }

        line = f"[{timestamp}] [{tag.upper()}] 🕶️ {message}"
        self.memory.append(entry)
        print(line)

        try:
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry) + "\n")
        except Exception as e:
            print(f"⚠️ Failed to write to log file: {e}")

        save_log("GhostScroll", "record", entry)

    def retrieve_logs(self, tag=None):
        if tag:
            return [e for e in self.memory if e["tag"] == tag]
        return self.memory

    def clear_memory(self):
        self.memory = []
        self.index = 0
        print("🧠 GhostScroll memory wiped clean.")

    def show_memory_pulse(self, limit=5):
        print("🩺 Memory Pulse:")
        for entry in self.memory[-limit:]:
            print(f"[{entry['timestamp']}] {entry['tag'].upper()} → {entry['message']}")

    def export_memory(self):
        return json.dumps(self.memory, indent=2)
