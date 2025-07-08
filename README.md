Uzbek Conversational AI Agent

This project implements a simple yet effective conversational AI agent designed to interact with users in Uzbek for lead qualification or information gathering. Built using the Google Agent Development Kit (ADK) and powered by the gemini-2.0-flash-exp model, the agent follows a structured conversation flow, saves user responses, and handles various conversational scenarios including rejections and out-of-topic replies.
Features

    Uzbek Language Support: The agent communicates entirely in Uzbek.

    Structured Conversation Flow: Guides users through a predefined sequence of questions.

    Dynamic Response Handling: Categorizes user responses as positive (ha), negative (yoq), indecisive (ikkilanish), or out-of-topic (out_of_topic).

    Data Persistence: Saves conversation data (question, user answer, and label) to a CSV file for each unique session.

    Rejection Logic: Gracefully ends the conversation if the user declines participation at specific key points.

    Out-of-Topic Repetition: Repeats the current question if the user's response is irrelevant.

    Scalable Architecture: Designed with the Google ADK for potential deployment in production environments.

Prerequisites

Before you begin, ensure you have the following installed:

    Python 3.9+

    Google Agent Development Kit (ADK):
    You can install it via pip:

    pip install google-adk

    Google Cloud Project and Credentials:
    You'll need a Google Cloud project with the Vertex AI API enabled and authenticated credentials configured for your environment (e.g., via gcloud auth application-default login). The gemini-2.0-flash-exp model is accessed through Vertex AI.

Project Structure

.
├── agent.py
├── saving.py
└── test.py
└── README.md

    agent.py: Contains the core AI agent logic, including its instructions, defined questions, and the integration with the saving.py module via a FunctionTool. This is where the conversational flow and decision-making are defined.

    saving.py: Provides a utility function (save_conversation_data_to_csv) responsible for persisting conversation data to CSV files. Each conversation session gets its own unique CSV file.

    test.py: Unit tests for the agent's conversational logic and its interaction with the saving module, using unittest.mock to simulate the ADK environment.

Installation

    Clone the repository:

    git clone https://github.com/your-username/uzbek-ai-agent.git
    cd uzbek-ai-agent

    (Replace your-username with your actual GitHub username or the repository URL.)

    Install dependencies:

    pip install google-adk

    Note: saving.py uses standard Python libraries (csv, os, uuid) and doesn't require additional pip installations beyond the ADK.

Usage

To run the agent, you typically use the ADK CLI. Ensure your Google Cloud credentials are set up and the Vertex AI API is enabled for your project.

    Navigate to the project directory:

    cd /path/to/your/uzbek-ai-agent

    Run the agent using the ADK CLI:

    adk web agent.py

    This command will usually launch a local web UI in your browser (e.g., http://localhost:8000 or http://127.0.0.1:8000) where you can interact with your agent.

    Alternatively, for command-line interaction:

    adk run agent.py

Example Conversation Flow (simulated):

Agent: "Assalomaleykum, men companiyadan qo'ng'iroq qiluvchi agentman. Malumbir loyihamizga qiziqish bildiribsiz, shu haqida gaplashishga vaqtingiz bormi?"
User: "Ha, vaqtim bor."
Agent: "Ajoyib, Hurmatli mijoz, ismingizni bilsam boladimi?."
User: "Mening ismim Dilshod."
Agent: "Ushbu loyihamiz haqida mutaxassislarimiz tomonidan to'liq ma'lumot olishni xohlaysizmi?"
User: "Ha, albatta!"
Agent: "Qiziqishingiz uchun rahmat! Mutaxassislarimiz siz bilan tez orada bog'lanishadi."

Rejection Scenario:

Agent: "Assalomaleykum, men companiyadan qo'ng'iroq qiluvchi agentman. Malumbir loyihamizga qiziqish bildiribsiz, shu haqida gaplashishga vaqtingiz bormi?"
User: "Yo'q, vaqtim yo'q."
Agent: "Suhbattingiz uchun rahmat, salomat bo'ling." (Conversation ends)

Out-of-Topic Scenario:

Agent: "Assalomaleykum, men companiyadan qo'ng'iroq qiluvchi agentman. Malumbir loyihamizga qiziqish bildiribsiz, shu haqida gaplashishga vaqtingiz bormi?"
User: "Bugun havo qanday?"
Agent: "Uzr, javobingizga tushunmadim. Savolni qaytaraman. Malumbir loyihamizga qiziqish bildiribsiz, shu haqida gaplashishga vaqtingiz bormi?"
Testing

The test.py file contains unit tests to verify the agent's logic without requiring a live ADK environment or a full LLM inference.

To run the tests:

    Navigate to the project directory:

    cd /path/to/your/uzbek-ai-agent

    Run the test file using Python's unittest module:

    python -m unittest test.py

The tests will simulate various conversation paths, including successful flows, rejections, and out-of-topic responses, verifying that the agent behaves as expected and calls the save_conversation_data_to_csv function with the correct arguments.
Configuration

You can easily modify the agent's behavior by editing the constants in agent.py:

    GREETING: The initial greeting message.

    AGENT_QUESTIONS: The sequence of questions the agent asks.

    CSV_QUESTION_KEYS: Corresponding keys for saving questions in the CSV.

    OUT_OF_TOPIC_RESPONSE: The message for out-of-topic replies.

    REJECT_RESPONSE: The message when a user rejects the conversation.

For more complex changes to the conversational logic, you would adjust the instruction string within the basic_agent definition in agent.py.
Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.
License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
