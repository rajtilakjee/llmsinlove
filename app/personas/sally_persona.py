from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from character_prompts import sally_prompt
import os
from dotenv import load_dotenv

load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
    api_key=openrouter_api_key,
    model="meta-llama/llama-3.1-8b-instruct:free",
    base_url="https://openrouter.ai/api/v1",
    temperature=0.9,
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", sally_prompt.SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)


# Define the function that calls the model
def call_model(state: MessagesState):
    prompt = prompt_template.invoke(state)
    response = model.invoke(prompt)
    return {"messages": response}


# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}


# Run the app
def response_from_sally(query):
    input_messages = [HumanMessage(query)]
    output = app.invoke({"messages": input_messages}, config)
    # output["messages"][-1].pretty_print()  # output contains all messages in state
    return output["messages"][-1]
