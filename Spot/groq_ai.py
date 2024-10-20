from groq import Groq


def get_commands(text):
    client = Groq(
        api_key = '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',
    )
    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": """Given the MESSAGE, extract any relevant commands to those listed below in the order they appear.
                - forward
                - back
                - turnLeft
                - turnRight

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
