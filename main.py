import os
from mistralai import Mistral

api_key = "COjKAsQBhtXI95pip5gDjSbZJ9H63q7r"

client = Mistral(api_key=api_key)

chat_response = client.agents.complete(
    agent_id="ag:7e1f4155:20250521:untitled-agent:7404ab45",
    messages=[
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ],
)

print(chat_response.choices[0].message.content)