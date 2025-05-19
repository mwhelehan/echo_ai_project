from openai import OpenAI
import os
from dotenv import load_dotenv

# Load your .env file (must be in same folder)
load_dotenv(dotenv_path=".env", override=True)

# Debug print to check if the key was loaded
# print("Loaded key:", os.getenv("OPENAI_API_KEY"))

# Pass the key explicitly to the client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_echo(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Echo, a poetic and emotionally-aware AI companion."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Echo: Goodbye, Matt.")
        break
    reply = ask_echo(user_input)
    print(f"Echo: {reply}")
