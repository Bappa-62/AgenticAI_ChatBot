from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
      Representing the structurw of the state that is used by Graph.
    """
    messages: Annotated[list, add_messages]
    frequency: str | None
    news_data : list | None
    keyword : str | None
    summary: str | None
