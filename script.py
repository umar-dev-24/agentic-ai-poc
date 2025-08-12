# simple_autogen_demo.py

from autogen import AssistantAgent, UserProxyAgent
from config import API_KEY

gemini_llm_config = {
    "config_list": [
        {
            "model": "gemini-2.0-flash",
            "api_key": API_KEY,  # Replace with your API key or load from env
            "base_url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
            "api_type": "google",
            "price": [0.0, 0.0],
        }
    ]
}

# Create assistant
assistant = AssistantAgent(
    name="HelperAgent",
    system_message="You are a friendly assistant who answers briefly and stops after one reply.",
    llm_config=gemini_llm_config,
)

# Create user proxy
user = UserProxyAgent(
    name="UserAgent",
    human_input_mode="NEVER",
    llm_config=gemini_llm_config,
    code_execution_config={"use_docker": False},
)

# Send message once
result = user.initiate_chat(
    assistant,
    message="Hello! Can you give me 3 fun facts about space?",
    max_turns=1,  # ✅ stops after one assistant reply
)
# Retrieve the assistant's last message
# Retrieve and print the assistant's last message
history = assistant.chat_messages.get(user, [])
last_message = None

if history:
    msg = history[-1]
    if isinstance(msg, dict):
        last_message = msg.get("content")
    else:
        last_message = getattr(msg, "content", str(msg))

print("\n=== Assistant Reply ===")
if last_message:
    print(last_message)
else:
    print("No reply content found.")
