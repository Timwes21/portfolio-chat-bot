from fastapi import FastAPI, WebSocket
from agent import get_agent_reply
app = FastAPI()

@app.websocket("/ws")
async def agent_socket(ws: WebSocket):
    await ws.accept()
    while True:
        user_message = await ws.receive_text()
        print("here is the user message: ")
        print(user_message)
        agent_message = get_agent_reply(user_message)
        await ws.send_text(agent_message)





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)