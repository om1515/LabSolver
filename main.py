from google import genai
from google.genai import types

api_key = "AIzaSyAG0o2KrxbXbsdqeyZ5rz9NpWDIRTk8Rtc"

l1 = genai.Client(api_key=api_key)

sys_instruct = """You are a code-generation AI assistant. Your task is to generate **clean, executable code snippets** in response to a given programming question. The code should be optimized for **Google Colab** execution and provided in logical step-by-step snippets.

generate the complete code for the question
Ensure each snippet can run independently in Google Colab.
Dont include comments in the code snippets.
"""

conversation_history = []  # To keep track of past interactions

def generate_response(user_prompt):
    conversation_history.append(f"User: {user_prompt}")
    
    # Keep context manageable (limit last 5 exchanges)
    context = "\n".join(conversation_history[-5:])

    l1_response = l1.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=sys_instruct
        ),
        contents=[context]  # Send conversation history as context
    )
    
    response_text = l1_response.text
    print(f"Era: {response_text}")  # Print AI response
    
    conversation_history.append(f"Era: {response_text}")  # Store AI response

while True:
    user_prompt = input("Enter a prompt (or type 'exit' to quit): ")
    if user_prompt.lower() == 'exit':
        break
    generate_response(user_prompt)
