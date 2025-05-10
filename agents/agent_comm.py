# agents/agent_comm.py – PhantomAgent Communication Hub (💠 SIGN 2.0 Upgrade)
# ------------------------------------------------------------------------------
# CENTRAL SIGNAL RELAY FOR ALL AGENTS – BUILT UNDER SIGN 2.0
# VOICE. SIGNAL. MEMORY. PURPOSE.
# ENGINEERED BY: PROFESSOR JOHNNY AI – 2025
# ------------------------------------------------------------------------------

from datetime import datetime

class AgentComm:
    def __init__(self):
        self.messages = []
        self.agents = set()
        self.channel_history = {}

    def broadcast(self, sender, channel, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = {
            "timestamp": timestamp,
            "sender": sender,
            "channel": channel,
            "message": message
        }
        self.messages.append(msg)
        self.agents.add(sender)

        if channel not in self.channel_history:
            self.channel_history[channel] = []
        self.channel_history[channel].append(msg)

        print(f"📡 [{timestamp}] [{channel}] {sender} → {message}")

    def retrieve(self, channel=None, sender=None):
        filtered = self.messages
        if channel:
            filtered = [m for m in filtered if m["channel"] == channel]
        if sender:
            filtered = [m for m in filtered if m["sender"] == sender]
        return filtered

    def recent_channels(self, limit=5):
        return list(self.channel_history.keys())[-limit:]

    def agent_roster(self):
        return list(self.agents)

    def clear(self):
        self.messages = []
        self.channel_history = {}
        self.agents = set()
        print("🧹 Communication memory wiped.")

    def replay_channel(self, channel):
        if channel not in self.channel_history:
            print(f"⚠️ No messages in channel: {channel}")
            return
        print(f"📼 Replay: Channel [{channel}]")
        for msg in self.channel_history[channel]:
            print(f"{msg['timestamp']} | {msg['sender']} → {msg['message']}")
