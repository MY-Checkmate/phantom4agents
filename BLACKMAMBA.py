# agents/BLACKMAMBA.py – Self-Mutating In-Memory Payload Executor (⚡ SIGN 2.0)
# --------------------------------------------------------------------------------
# “A payload that never looks the same twice, but always kills the same way.”
# AUTHOR: PROFESSOR JOHNNY AI | UNIT: SIGN 2.0 | YEAR: 2025
# --------------------------------------------------------------------------------


from PhantomAgentBase import PhantomAgentBase
import random
import hashlib
import base64

class BLACKMAMBA(PhantomAgentBase):
    def __init__(self):
        super().__init__("BLACKMAMBA")
        self.mutation_log = []
        self.signature_memory = []
        self.preview_mode = False  # When True, shows code instead of running

    def execute(self):
        print("🐍 BLACKMAMBA active – memory execution initiated.")
        if not self.mission:
            print("❌ No mission assigned.")
            return

        payload = self.mission.get("code", "print('🖤 Hello from BLACKMAMBA')")
        mutation_depth = self.mission.get("mutations", 3)
        self.preview_mode = self.mission.get("preview", False)

        mutated = self.mutate_payload(payload, mutation_depth)

        if self.preview_mode:
            print("👁️ Preview Mode Active (No Execution):")
            print(mutated)
        else:
            print("⚙️ Executing Payload in Memory...")
            exec(mutated)

        signature = hashlib.md5(mutated.encode()).hexdigest()
        self.signature_memory.append(signature)
        self.logs.append({"executed": not self.preview_mode, "hash": signature})
        print(f"🧬 Signature [{len(self.signature_memory)}]: {signature}")

    def mutate_payload(self, code, times):
        for i in range(times):
            encoded = base64.b64encode(code.encode()).decode()
            mutation = f"import base64; exec(base64.b64decode('{encoded}').decode())"
            self.mutation_log.append(f"🔁 Mutation {i+1}: {encoded[:10]}...")  # Log partial
            code = mutation
        return code

    def report(self):
        print("🧾 BLACKMAMBA Mutation Report:")
        for entry in self.mutation_log:
            print(entry)
        print(f"🧬 Total Signatures: {len(self.signature_memory)}")
