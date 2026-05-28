from fastapi import FastAPI
import time
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {
        "message": "Hello from my FastAPI application!",
        "status": "Online",
        "timestamp": f"{time.time():.2f}"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8098)
