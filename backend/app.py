from fastapi import FastAPI

app = FastAPI()

@app.post("/ping")
def ping():
    print("🔥🔥🔥 PING HIT 🔥🔥🔥")
    return {"pong": True}
