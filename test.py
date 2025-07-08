# test.py
import sys
import os
import io
import contextlib

print("Starting checks for Agent and Saving modules...\n")

# Add the project root to PYTHONPATH so saving.py can be found
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

try:
    from google.adk.agents import Agent
    from google.adk.tools import FunctionTool
    print("✅ Successfully imported google.adk.agents and google.adk.tools.")
except ImportError as e:
    print(f"❌ Error: google-adk is not installed or not found. Please run `pip install google-adk`. Error: {e}")
    sys.exit(1) # Stop the test if core libraries aren't found

try:
    from saving import save_conversation_data_to_csv
    print("✅ Successfully imported saving.py file and save_conversation_data_to_csv function.")
except ImportError as e:
    print(f"❌ Error: saving.py file not found or there was an issue importing it. Ensure it's in the same directory. Error: {e}")
    sys.exit(1)

try:
    from agent import AGENT_QUESTIONS, CSV_QUESTION_KEYS
    print("✅ Successfully imported AGENT_QUESTIONS and CSV_QUESTION_KEYS from agent.py file.")
except ImportError as e:
    print(f"❌ Error: agent.py file not found or there was an issue importing it. Error: {e}")
    sys.exit(1)

def run_tests():
    print("\n--- Testing save_conversation_data_to_csv function ---")
    test_session_id = "test_session_123"
    test_question_key = "Test Question"
    test_user_answer = "This is a test answer."
    test_label = "ha" # Using 'ha' as an example label

    # Capture print output temporarily
    with contextlib.redirect_stdout(io.StringIO()) as buffer:
        result = save_conversation_data_to_csv(test_session_id, test_question_key, test_user_answer, test_label)
    output = buffer.getvalue().strip()

    if "muvaffaqiyatli saqlandi" in result and "label: 'ha'" in result:
        print(f"✅ save_conversation_data_to_csv function works correctly: {result}")
        # Clean up the test file
        try:
            # Access the global variable from the saving module to get the actual file name created
            from saving import _session_file_map
            actual_test_file_name = _session_file_map.get(test_session_id)
            if actual_test_file_name and os.path.exists(actual_test_file_name):
                os.remove(actual_test_file_name)
                print(f"   (Successfully cleaned up test file: '{actual_test_file_name}')")
            else:
                print(f"   (Could not find/delete test file: {actual_test_file_name})")
        except Exception as e:
            print(f"   (Unexpected error while cleaning up test file: {e})")
    else:
        print(f"❌ save_conversation_data_to_csv function did not work as expected. Result: {result}")
        print(f"   Output messages (if any): {output}")


    print("\n--- Testing FunctionTool object creation ---")
    try:
        test_tool = FunctionTool(func=save_conversation_data_to_csv)
        print("✅ FunctionTool object created successfully.")
    except Exception as e:
        print(f"❌ Error creating FunctionTool object: {e}")

    print("\n--- Testing Agent object initialization ---")
    try:
        # Import the basic_agent directly from agent.py
        from agent import basic_agent
        print("✅ Agent object loaded and initialized successfully.")
        # Check if the tool is correctly attached
        if basic_agent.tools and basic_agent.tools[0].func == save_conversation_data_to_csv:
            print("✅ 'save_data_tool' is correctly attached to the Agent.")
        else:
            print("⚠️ 'save_data_tool' might not be correctly attached to the Agent or not found.")

    except Exception as e:
        print(f"❌ Error initializing Agent object: {e}")

    print("\n--- All basic checks complete ---")
    print("If there are no '❌' errors above, your project's basic structure is sound.")
    print("You can now proceed to run your agent in the ADK web environment for full testing.")

if __name__ == "__main__":
    run_tests()