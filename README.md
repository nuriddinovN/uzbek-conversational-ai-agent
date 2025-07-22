# 🇺🇿 Uzbek Conversational AI Agent

A lightweight, structured conversational AI built with the [Google Agent Development Kit (ADK)](https://github.com/google/agent-development-kit) and powered by the **Gemini 2.0 Flash** model. This agent communicates **entirely in Uzbek**, conducts a multi-step dialogue, classifies user intent, and stores all session data for lead qualification, surveys, or information gathering.

---

## 🚀 Features

- 🗣️ **Uzbek Language Support**  
  Fully localized interaction in Uzbek for native communication.

- 🔁 **Structured Question Flow**  
  Follows a predefined conversational path with customizable prompts.

- 🤖 **Intelligent Classification**  
  Detects and labels user responses as:
  - `ha` (positive)
  - `yo‘q` (negative)
  - `ikkilanish` (uncertain)
  - `out_of_topic` (irrelevant)

- 🧠 **Rejection and Repetition Logic**  
  Handles "no" responses gracefully and repeats questions if the user goes off-topic.

- 💾 **Data Persistence**  
  Logs each session’s questions, user responses, and labels into a unique `.csv` file.

- ⚙️ **Scalable ADK Architecture**  
  Easily extendable and deployable via Google ADK.

---

## 🧱 Project Structure

```
uzbek-ai-agent/
├── agent.py                # Main agent script with flow logic and tools
├── saving.py               # Utility for saving conversation data to CSV
├── test.py                 # Unit tests for agent behavior
└── README.md               # This documentation
```

---

## 📦 Installation

> Ensure you are using **Python 3.9+**

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/uzbek-ai-agent.git
cd uzbek-ai-agent
```

2. **Install dependencies**:
```bash
pip install google-adk
```

3. **Set up Google Cloud credentials**:
- Enable **Vertex AI API** in your Google Cloud project.
- Authenticate using:
```bash
gcloud auth application-default login
```
- Make sure your `GOOGLE_APPLICATION_CREDENTIALS` environment variable points to your credentials JSON file.

---

## ▶️ Usage

### 🔗 Web Interface
Launch the agent using ADK’s web interface:
```bash
adk web agent.py
```
This will open a local browser window at `http://127.0.0.1:8000` or similar.

### 🖥️ CLI Interface
Alternatively, run the agent directly in the terminal:
```bash
adk run agent.py
```

---

## 💬 Sample Conversation (Simulated)

```text
Agent: Assalomaleykum, men kompaniyadan qo'ng'iroq qiluvchi agentman. Loyihamizga qiziqish bildirgansiz. Suhbatlashishga vaqtingiz bormi?
User: Ha, vaqtim bor.
Agent: Ajoyib. Ismingizni bilsam bo'ladimi?
User: Mening ismim Dilshod.
Agent: Loyihamiz haqida mutaxassislarimizdan to'liq ma’lumot olishni xohlaysizmi?
User: Ha, albatta!
Agent: Qiziqishingiz uchun rahmat! Mutaxassislarimiz siz bilan tez orada bog'lanishadi.
```

### ❌ Rejection Scenario
```text
User: Yo‘q, hozir vaqtim yo‘q.
Agent: Suhbat uchun rahmat. Salomat bo‘ling!
```

### ❓ Out-of-Topic Scenario
```text
User: Bugun havo qanday?
Agent: Uzr, savolingiz mavzudan tashqarida. Savolni qaytaraman: Loyihamizga qiziqish bildirgansiz. Suhbatlashishga vaqtingiz bormi?
```

---

## 🧪 Testing

Run unit tests to validate flow logic and saving behavior:

```bash
python -m unittest test.py
```

The test cases simulate:
- Valid user flows
- Rejections
- Out-of-topic responses
- Data-saving integrity via mocks

---

## 🔧 Configuration

You can customize the agent behavior by editing variables in `agent.py`:

| Variable | Description |
|----------|-------------|
| `GREETING` | Initial welcome message |
| `AGENT_QUESTIONS` | List of sequential questions |
| `CSV_QUESTION_KEYS` | CSV column headers |
| `OUT_OF_TOPIC_RESPONSE` | Message for irrelevant answers |
| `REJECT_RESPONSE` | Exit message when user declines |

To modify decision logic, update the `basic_agent` instructions accordingly.

---

## 📁 Data Output Format

Each session generates a CSV file named with a unique UUID, containing:

| Question | User Response | Label |
|----------|----------------|-------|
| "Ismingizni bilsam bo'ladimi?" | "Dilshod" | "ha" |
| "Mutaxassislarimiz bilan suhbatlashishni xohlaysizmi?" | "Ha" | "ha" |
| ... | ... | ... |

---

## 🤝 Contributing

Contributions are welcome! If you find bugs, have ideas, or want to extend functionality (e.g., adding audio support, advanced STT/TTS, or deployment on serverless), feel free to open an issue or submit a pull request.

---

