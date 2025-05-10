# agents/PhantomAgentBase.py – Shared AI Brain for All Agents

import requests
import socket
from scapy.all import sniff
from datetime import datetime
from ops.mission_center import get_mission  # Adjusted path

class PhantomAgentBase:
    def __init__(self, agent_name):
        self.name = agent_name
        self.mission = get_mission(agent_name)
        self.logs = []

    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [{self.name}] {message}")
        self.logs.append(f"{timestamp} | {message}")

    def execute(self):
        if not self.mission:
            self.log("❌ No mission assigned.")
            return

        action = self.mission.get("mission")
        method = getattr(self, action, None)
        if callable(method):
            self.log(f"🧠 Executing mission: {action}")
            method()
        else:
            self.log(f"⚠️ Unknown mission type: {action}")

    def scan(self):
        ip = self.mission.get("ip")
        self.log(f"📡 Scanning: {ip}")
        result = {}

        try:
            hostname = socket.gethostbyaddr(ip)[0]
            result["hostname"] = hostname
        except:
            result["hostname"] = "unknown"

        try:
            r = requests.get(f"http://{ip}", timeout=4)
            result["http_status"] = r.status_code
            result["server"] = r.headers.get("Server", "unknown")
            result["powered_by"] = r.headers.get("X-Powered-By", "unknown")
        except:
            result["http_status"] = "no response"

        self.log(f"🧠 Scan Result: {result}")

    def strike(self):
        ip = self.mission.get("ip")
        payload = self.mission.get("payload")
        if not ip or not payload:
            self.log("❌ Strike mission incomplete.")
            return
        self.log(f"💥 Executing payload '{payload}' on {ip}...")

    def phish(self):
        url = self.mission.get("url")
        if not url:
            self.log("❌ No URL provided for phishing.")
            return
        self.log(f"🎣 Lure deployed at: {url}")

    def sniff(self):
        count = self.mission.get("packet_count", 10)
        self.log(f"👁️ Sniffing {count} packets...")

        def callback(pkt):
            try:
                info = {
                    "time": str(datetime.now()),
                    "src": pkt[0][1].src if hasattr(pkt[0][1], "src") else "unknown",
                    "dst": pkt[0][1].dst if hasattr(pkt[0][1], "dst") else "unknown",
                    "proto": pkt[0][1].name if hasattr(pkt[0][1], "name") else "unknown"
                }
                self.logs.append(info)
                self.log(f"👁️ Packet: {info}")
            except Exception as e:
                self.log(f"⚠️ Error: {e}")

        sniff(prn=callback, count=count, store=False)
