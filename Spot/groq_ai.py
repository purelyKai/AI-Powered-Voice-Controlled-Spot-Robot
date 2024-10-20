from groq import Groq
from config import Config


def get_commands(text):
    client = Groq(
        api_key = Config.Spot_Groq_Api_Key,
    )
    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": """Given the MESSAGE, extract any relevant commands to those listed below in the order they appear.
                - forward
                - back 
                - turnLeft
                - turnRight. 

                Respond with only the commands mentioned in the MESSAGE below
                
                """

            },
            {
            "role":"user",
            "content":f"MESSAGE: {text}",
            
            }
        ],
        model = "llama-3.1-70b-versatile",
    )
    print(chat_completion.choices[0].message.content)
    
    return chat_completion.choices[0].message.content


get_commands("Why do you move ahead, maybe turn to the left and then move backwards")
