# agents/SilentFox_AI.py – DNS Tunneling Recon + Stealth Scanner (SIGN 2.0 Upgrade)
# ------------------------------------------------------------------------------
# SILENT. SMART. SURGICAL.
# ENGINEERED BY: PROFESSOR JOHNNY AI | DIVISION: SIGN 2.0
# ------------------------------------------------------------------------------
from PhantomAgentBase import PhantomAgentBase
import random
import time
from datetime import datetime

class SilentFoxAI(PhantomAgentBase):
    def __init__(self):
        super().__init__("SilentFox")
        self.scan_log = []
        self.last_signature = None

    def execute(self):
        print("🦊 SilentFox engaged – DNS stealth probe initiated.")
        if not self.mission:
            print("❌ No mission assigned.")
            return

        domain = self.mission.get("dns_target", "phantom.sandbox.local")
        scan_depth = self.mission.get("scan_depth", 3)
        recursive = self.mission.get("recursive_mode", False)

        print(f"🌐 Probing {domain} (depth={scan_depth}, recursive={recursive})")
        responses = []

        for i in range(scan_depth):
            time.sleep(0.7)
            subquery = f"stage{i}.{domain}"
            response = self.dns_query(subquery)
            category = self.categorize_response(response)

            probe = {
                "query": subquery,
                "response": response,
                "category": category,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.logs.append(probe)
            self.scan_log.append(probe)
            responses.append(response)
            print(f"🛰️ [{i+1}/{scan_depth}] {subquery} → {response} ({category})")

            if recursive and response.startswith("192."):
                domain = f"link{i}.{domain}"

        # Save tunnel signature
        self.last_signature = hash("".join(responses)) % 999999
        print(f"🔏 Tunnel Signature: SIG-{self.last_signature}")

    def dns_query(self, subdomain):
        simulated_ips = ["192.168.0.1", "10.0.0.5", "172.16.1.3", "NXDOMAIN", "REFUSED"]
        return random.choice(simulated_ips)

    def categorize_response(self, response):
        if "192." in response or "10." in response:
            return "🟢 Internal"
        elif "172." in response:
            return "🟡 DMZ"
        elif "NXDOMAIN" in response:
            return "🔴 Dead Node"
        elif "REFUSED" in response:
            return "⚠️ Blocked"
        return "⚪ Unknown"

    def get_last_signature(self):
        return f"SIG-{self.last_signature}" if self.last_signature else "🌀 No scans yet."

    def scan_digest(self, limit=5):
        return self.scan_log[-limit:] if self.scan_log else ["🌀 No scan logs yet."]
