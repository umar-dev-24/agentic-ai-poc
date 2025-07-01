def get_llm_config():
    return [
        {
            "model": "mistral",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama_not_needed",
        }
    ]
