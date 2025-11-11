from dependency_injector import containers, providers
from app.agent.research_agent.research_agent import ResearchAgent

class Container(containers.DeclarativeContainer):
    research_agent_container = providers.Singleton(
        ResearchAgent
    )