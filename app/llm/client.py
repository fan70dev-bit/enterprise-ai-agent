from app.llm.deepseek import chat


class LLMClient:

    def chat(
        self,
        messages: list,
    ):

        return chat(messages)


llm = LLMClient()