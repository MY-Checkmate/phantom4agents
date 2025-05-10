# agents/SniffSpectre_AI.py – Live Packet Sniffer Agent (SIGN 2.0 Recon Upgrade)
# ------------------------------------------------------------------------------
# 👁️ BUILT TO SEE THE UNSEEN. BUILT FOR PACKET GHOSTING.
# ENGINEERED BY: PROFESSOR JOHNNY AI | UNIT: SIGN 2.0
# ------------------------------------------------------------------------------
from PhantomAgentBase import PhantomAgentBase
from ops.log_manager import save_log
from scapy.all import sniff
from datetime import datetime

class SniffSpectreAI(PhantomAgentBase):
    def __init__(self):
        super().__init__("SniffSpectre")
        self.packet_memory = []

    def deep_sniff(self, packet_count=20, iface=None, filter_expr=None):
        self.log(f"👁️ Listening for {packet_count} packets...")

        def callback(pkt):
            try:
                layer = pkt.getlayer(1)
                info = {
                    "timestamp": str(datetime.now()),
                    "src": getattr(layer, "src", "unknown"),
                    "dst": getattr(layer, "dst", "unknown"),
                    "proto": layer.name if hasattr(layer, "name") else "unknown",
                    "len": len(pkt),
                    "summary": pkt.summary()
                }

                # 🧠 Tag suspicious patterns
                if "FTP" in pkt.summary() or pkt.dport in [21, 23, 445]:
                    info["tag"] = "⚠️ Suspicious Port Use"

                self.packet_memory.append(info)
                self.logs.append(info)
                self.log(f"📡 Packet: {info}")
                save_log(self.name, "sniff", info)

            except Exception as e:
                self.log(f"⚠️ Sniff error: {e}")

        sniff(prn=callback, count=packet_count, store=False, iface=iface, filter=filter_expr)

    def packet_digest(self, limit=10):
        print(f"🧾 SniffSpectre Packet Digest (Last {limit}):")
        for p in self.packet_memory[-limit:]:
            print(f"[{p['timestamp']}] {p['src']} ➜ {p['dst']} ({p['proto']}) | {p.get('tag', '✅ Clean')}")

    def export_capture(self):
        return self.packet_memory
