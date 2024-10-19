from groq import Groq
from config import Config

client = Groq(
    api_key = Config.Spot_Groq_Api_Key,

)

chat_completion = client.chat.completions.create(
    messages = [
        {
        "role":"user",
        "content":"Explain the importance of fast language models",
        }

    ],
    model = "llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)