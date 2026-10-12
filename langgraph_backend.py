from langgraph.graph import StateGraph,START,END, add_messages
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from typing import TypedDict , Literal , Annotated , List
from pydantic import BaseModel , Field
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph .checkpoint.memory import MemorySaver

load_dotenv(override=True)

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env. Please check your .env file.")

# Initialize Chat Model
# Using Gemini with the active GOOGLE_API_KEY from .env
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=api_key,
    temperature=0.7,
)


# from langgraph.graph import add_messages


# class ChatState(TypedDict):
#     messages : Annotated[list[BaseModel], add_messages]


# def chat_node(state: ChatState):
#     messages = state['messages']
#     response =model.invoke(messages)
#     return {'messages' : [response]}

# checkpointer = MemorySaver()
# graph = StateGraph(ChatState)

# graph.add_node('chat_node',chat_node)

# graph.add_edge(START,'chat_node')
# graph.add_edge('chat_node',END)

# workflow = graph.compile(checkpointer=checkpointer)


# from langgraph.graph import StateGraph, START, END
# from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
# # from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
# from langgraph.graph.message import add_messages
# from dotenv import load_dotenv

load_dotenv()

# llm = ChatOpenAI()

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = model.invoke(messages)
    return {"messages": [response]}

# Checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)