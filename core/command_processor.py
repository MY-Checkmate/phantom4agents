import subprocess
from core.ai_engine import AIEngine

class CommandProcessor:
    def __init__(self):
        self.ai_engine = AIEngine()

    def process(self, command):
        # Recon command integration
        if command.startswith('recon '):
            target_url = command.replace('recon ', '').strip()
            try:
                # Trigger the advanced_recon.js script with the target URL
                result = subprocess.run(
                    ['node', './modules/pentesting/advanced_recon.js', target_url],
                    capture_output=True,
                    text=True
                )
                return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
            except Exception as e:
                return f"Recon error: {e}"

        # Scrape command integration
        elif command.startswith('scrape '):
            url = command.replace('scrape ', '').strip()
            try:
                from modules.scraping.simple_scraper import scrape_links
                links = scrape_links(url)
                return '\n'.join(links) if links else 'No links found.'
            except Exception as e:
                return f"Scraping error: {e}"

        # Use the AI engine to process other commands
        return self.ai_engine.process_command(command)

    def process_voice_command(self, command):
        # Map voice commands to system commands
        if "run scan" in command:
            return self.process("scan")
        elif "generate report" in command:
            return self.process("report")
        elif "check memory" in command:
            return self.process("memory")
        elif "alert" in command:
            return self.process("alert")
        else:
            return "Command not recognized."
