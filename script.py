from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
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
assistant1 = AssistantAgent(
    name="HelperAgent",
    system_message="You are a friendly assistant who answers briefly and stops after one reply.",
    llm_config=gemini_llm_config,
)

assistant2 = AssistantAgent(
    name="ScienceAgent",
    system_message="You are a scientist who gives one planet name in space when your turn comes.",
    llm_config=gemini_llm_config,
)

assistant3 = AssistantAgent(
    name="FunAgent",
    system_message="You share fun and surprising one fact about a given planet.",
    llm_config=gemini_llm_config,
)

# Create user proxy
user = UserProxyAgent(
    name="UserAgent",
    human_input_mode="NEVER",
    llm_config=gemini_llm_config,
    code_execution_config={"use_docker": False},
)

# Create a group chat with required agents
group_chat = GroupChat(
    agents=[user, assistant2, assistant3],
    messages=[],
    max_round=3,  # total loop limit
)

# Create group chat manager
manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=gemini_llm_config,
)


# Start the single chat using below snippet
user.initiate_chat(
    assistant1,
    message="Hello! Can you give me 3 fun facts about space?",
    max_turns=1,  # ✅ stops after one assistant reply
)


# Start the group chat using below snippet
# user.initiate_chat(
#     manager, message="Let’s discuss the most fascinating facts about space."
# )


"""
You can create multiple assistants and user proxies, and then add them in group chat.
Run "pip install pyautogen" to install the autogen package.
Replace the API_KEY with your actual API key from Google Cloud for Gemini.
"""
