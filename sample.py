from ollama import chat

response = chat(
    model='llama3.2:latest',
    messages=[{'role': 'user', 'content': 'What is a meaning of Catalyst'}],
)
print(response.message.content)