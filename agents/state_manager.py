# agents/state_manager.py – Real-time Agent State Tracker (SIGN 2.0 Upgrade)
# ------------------------------------------------------------------------------
# CORE MEMORY MAP FOR ALL SIGN 2.0 AI AGENTS
# ENGINEERED BY: PROFESSOR JOHNNY AI | YEAR: 2025
# ------------------------------------------------------------------------------

from datetime import datetime
import json

class StateManager:
    def __init__(self):
        self.state = {}
        self.heartbeat = {}

    def update_state(self, agent, key, value):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if agent not in self.state:
            self.state[agent] = {"_log": [], "_versions": []}

        # Update state and store version snapshot
        self.state[agent][key] = value
        self.state[agent]["_log"].append(f"[{timestamp}] {key} → {value}")
        snapshot = {k: v for k, v in self.state[agent].items() if not k.startswith("_")}
        self.state[agent]["_versions"].append({
            "timestamp": timestamp,
            "snapshot": snapshot
        })

        # Heartbeat ping
        self.heartbeat[agent] = timestamp
        print(f"🧬 {agent} updated → {key}: {value}")

    def get_state(self, agent):
        return self.state.get(agent, {})

    def get_log(self, agent):
        return self.state.get(agent, {}).get("_log", [])

    def get_versions(self, agent, limit=5):
        return self.state.get(agent, {}).get("_versions", [])[-limit:]

    def clear_agent(self, agent):
        if agent in self.state:
            del self.state[agent]
        if agent in self.heartbeat:
            del self.heartbeat[agent]
        print(f"🧹 State cleared for: {agent}")

    def global_state_dump(self):
        clean_state = {agent: {k: v for k, v in data.items() if not k.startswith("_")}
                       for agent, data in self.state.items()}
        return clean_state

    def export_as_json(self):
        return json.dumps(self.global_state_dump(), indent=2)

    def status_summary(self):
        print("📡 Agent Heartbeat Summary:")
        for agent, ts in self.heartbeat.items():
            print(f"🧠 {agent} → Last update: {ts}")
