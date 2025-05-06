from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPEN_AI_API_KEYS")
vector_id = os.getenv("VECTOR_ID")


client = OpenAI(api_key=api_key)



def get_agent_reply(user_message):
    
    input = [
        {
            "role": "developer",
            "content": "You are being used in my portfolio to mimic me, try to act like me and answer questions about me as if you are me"
        },
        {
            "role": "user",
            "content":  user_message         
        }
    ]
    
    tools = [{
            "type": "file_search",
            "vector_store_ids": [vector_id]
        }]
    
    response = client.responses.create(
        model="gpt-4o-mini",
        input= input,
        tools =tools
    )
    
    return response.output_text

reply = get_agent_reply("how old are you")
print(reply)
    