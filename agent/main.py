from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.container.container import Container


# Initialize the dependency injection container
container = Container()

# Wire the container to inject dependencies into the modules
# IMPORTANT: Wire BEFORE importing routers
# Only wire the dependencies module, not the router module
container.init_resources()
container.wire(
    modules=[
        __name__,
        "app.api.dependencies",  # Wire to dependencies module only
    ]
)

# Import routers AFTER wiring
from app.api.router.chat import router as chat_router

app = FastAPI()

# Store container in app state for lifecycle management
app.state.container = container

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
