from fastapi import FastAPI
from agent import Agent10
app = FastAPI(title="Creative-Writing-CoAuthor")
agent = Agent10()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
