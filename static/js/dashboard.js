// Fetch agent statuses
async function fetchAgentStatus() {
  const response = await fetch('/agents/status');
  const agents = await response.json();
  const agentList = document.getElementById('agent-list');
  agentList.innerHTML = '';
  agents.forEach(agent => {
    const li = document.createElement('li');
    li.textContent = `${agent.name}: ${agent.status}`;
    agentList.appendChild(li);
  });
}

// Send a command
async function sendCommand(command) {
  const response = await fetch('/agents/command', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ command })
  });
  const result = await response.json();
  document.getElementById('log-output').textContent += `\n${result.result}`;
}

// Fetch logs
async function fetchLogs() {
  const response = await fetch('/logs');
  const logs = await response.json();
  const logOutput = document.getElementById('log-output');
  logOutput.textContent = logs.join('\n');
}

// Initialize voice command
function initVoiceCommand() {
  const micButton = document.getElementById('voice-command');
  micButton.addEventListener('click', () => {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = (event) => {
      const voiceCommand = event.results[0][0].transcript;
      document.getElementById('command-input').value = voiceCommand;
      sendCommand(voiceCommand);
    };

    recognition.onerror = (err) => {
      console.error('Voice Recognition Error:', err);
    };
  });
}

// Initialize chart
function initChart() {
  const ctx = document.getElementById('results-chart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['High Priority', 'Medium Priority', 'Low Priority'],
      datasets: [{
        label: 'Recon Results',
        data: [12, 19, 3], // Example data
        backgroundColor: ['red', 'orange', 'yellow']
      }]
    }
  });
}

// Initialize dashboard
function initDashboard() {
  fetchAgentStatus();
  fetchLogs();
  initVoiceCommand();
  initChart();

  document.getElementById('send-command').addEventListener('click', () => {
    const command = document.getElementById('command-input').value;
    sendCommand(command);
  });

  // Refresh agent status and logs every 5 seconds
  setInterval(fetchAgentStatus, 5000);
  setInterval(fetchLogs, 5000);
}

document.addEventListener('DOMContentLoaded', initDashboard);