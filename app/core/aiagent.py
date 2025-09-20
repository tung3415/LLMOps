from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
from app.config.settings import settings

def get_response_from_ai_agents(model_name, query, allow_search, system_prompt):

    llm = ChatGroq(model=model_name)
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    state = {"messages": query}

    agent = create_react_agent(
        model = llm,
        tools = tools,
        prompt= system_prompt
    )

    response = agent.invoke(state)
    messages = response.get("messages")

    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

    return ai_messages[-1]





