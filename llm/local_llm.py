from langchain_ollama import ChatOllama


def run_local_llm(prompt: str) -> str:
    llm = ChatOllama(model="mistral")  # You can change this to "phi3", etc.
    response = llm.invoke(prompt)
    if isinstance(response.content, list):
        # Join string elements, or convert dicts to string if needed
        result = " ".join(str(item) for item in response.content)
        return result.strip()
    return str(response.content).strip()
