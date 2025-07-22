# gemini_llm.py
# import requests

# API_KEY = "AIzaSyBeGSgimqzyb5je9P8L97EfkVVhSeav3eU"  # ✅ Replace this with env var in production
# ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
# HEADERS = {"Content-Type": "application/json"}


# def run_gemini(messages: list[dict]) -> str:
#     # Gemini API expects contents with role and parts
#     data = {"contents": messages}
#     response = requests.post(f"{ENDPOINT}?key={API_KEY}", headers=HEADERS, json=data)

#     if response.ok:
#         try:
#             return response.json()["candidates"][0]["content"]["parts"][0]["text"]
#         except Exception:
#             return str(response.json())
#     else:
#         return f"[Error] {response.status_code}: {response.text}"


# class GeminiLLM:
#     def __init__(self):
#         pass

#     def __call__(self, messages, **kwargs):
#         # Convert AutoGen-style messages to Gemini format
#         gemini_messages = []
#         for msg in messages:
#             if "role" in msg and "content" in msg:
#                 gemini_messages.append(
#                     {"role": msg["role"], "parts": [{"text": msg["content"]}]}
#                 )
#         return {"role": "assistant", "content": run_gemini(gemini_messages)}
config_list_gemini = [
    {
        "model": "gemini-1.5-flash-001",
        "api_type": "google",
        "api_key": "YOUR_GOOGLE_API_KEY",  # Replace with your API key or set up authentication.
    }
]

llm_config_gemini = {
    "config_list": config_list_gemini,
    "cache_seed": 42,  # optional
    "temperature": 0.0,  # optional
    # other llm parameters
}
