import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(token=HF_TOKEN)

print("AI Chatbot")
print("Type 'exit' to stop the chatbot.\n")

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Chatbot closed.")
        break

    response = client.chat_completion(
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ],
        model="meta-llama/Llama-3.1-8B-Instruct"
    )

    print("AI:", response.choices[0].message.content)
    print()