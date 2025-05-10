# agents/PhantomLure_AI.py – Lure / Phishing Deployment Agent (SIGN 2.0 Elite Backbone)
# -------------------------------------------------------------------------------------
# THIS IS THE PHANTOM'S BAIT. NOT A SCAM. A STRATEGIC TRAP.
# AUTHOR: PROFESSOR JOHNNY AI | YEAR 2025 | DIVISION: SIGN 2.0
# -------------------------------------------------------------------------------------

from agents.PhantomAgentBase import PhantomAgentBase
from ops.log_manager import save_log
import requests
from datetime import datetime
import random

class PhantomLureAI(PhantomAgentBase):
    def __init__(self):
        super().__init__("PhantomLure")
        self.lure_url = None
        self.deploy_log = []
        self.styles = ["clone", "spoof", "overlay", "geo-switch"]
        self.current_style = None
        self.fingerprint = f"PL-{random.randint(1000,9999)}"

    def deploy_lure(self, url=None, style=None):
        self.lure_url = url or self.mission.get("url")
        self.current_style = style or self.mission.get("style", random.choice(self.styles))

        if not self.lure_url:
            msg = "❌ No URL provided for lure deployment."
            self.log(msg)
            return msg

        try:
            response = requests.get(self.lure_url, timeout=5)
            result = {
                "fingerprint": self.fingerprint,
                "url": self.lure_url,
                "style": self.current_style,
                "status": response.status_code,
                "server": response.headers.get("Server", "unknown"),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.deploy_log.append(result)
            self.log(f"🎣 [{self.current_style}] Lure active at {self.lure_url} (status {response.status_code})")
        except Exception as e:
            result = {
                "fingerprint": self.fingerprint,
                "url": self.lure_url,
                "style": self.current_style,
                "status": "fail",
                "error": str(e),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.deploy_log.append(result)
            self.log(f"⚠️ [{self.current_style}] Lure failed at {self.lure_url}: {e}")

        save_log(self.name, "phish", result)
        return result

    def auto_execute(self):
        mission_url = self.mission.get("url")
        if mission_url:
            self.log("🔁 Auto-triggering deploy_lure from mission URL.")
            return self.deploy_lure(url=mission_url)
        else:
            self.log("🚫 No URL found in mission. Auto-execute skipped.")
            return "No mission URL available."

    def recent_deploys(self, count=5):
        return self.deploy_log[-count:] if self.deploy_log else ["🌀 No deployments yet."]

    def lure_summary(self):
        active = [d for d in self.deploy_log if d["status"] != "fail"]
        failed = [d for d in self.deploy_log if d["status"] == "fail"]
        return {
            "total_deploys": len(self.deploy_log),
            "success_count": len(active),
            "fail_count": len(failed),
            "last_style": self.current_style,
            "fingerprint": self.fingerprint
        }
