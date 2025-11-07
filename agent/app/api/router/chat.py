from fastapi import APIRouter

router = APIRouter()

@router.get("/chat")
def read_chat():
    return {"message": "This is the chat endpoint"}