from app.llm.deepseek import chat


result = chat(
    [
        {
            "role":"user",
            "content":"你好，你是谁？"
        }
    ]
)


print(result)