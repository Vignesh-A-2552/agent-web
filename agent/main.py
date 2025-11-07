from fastapi import FastAPI
import uvicorn
from app.router.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
