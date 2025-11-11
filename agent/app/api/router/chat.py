from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.agent.research_agent.research_agent import ResearchAgent
from app.api.dependencies import get_research_agent

router = APIRouter(prefix="/api/v1")




class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    query: str


class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    research_summary: str
    research_documents: str


@router.get("/chat")
def read_chat():
    """Simple GET endpoint for chat."""
    return {"message": "This is the chat endpoint"}


@router.post("/chat/research", response_model=ChatResponse)
async def research_chat(
    request: ChatRequest,
    agent: ResearchAgent=Depends(get_research_agent)
):
    """
    Research chat endpoint that uses the Research Agent.

    Args:
        request: ChatRequest containing the user query

    Returns:
        ChatResponse with research summary and documents
    """

    # Invoke the research agent
    result = await agent.invoke({"user_input": request.query})

    # Return a plain dictionary instead of ChatResponse object
    # This prevents FastAPI from trying to validate the complex LangGraph state
    return {
        "research_summary": result.get("research_summary", ""),
        "research_documents": result.get("research_documents", "")
    }