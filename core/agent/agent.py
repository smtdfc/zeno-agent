from typing import Any, Callable, Union, TypeAlias

from langchain.agents import create_agent
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, AIMessage

from core.agent.middlewares import handle_tool_errors
from core.agent.prompt import system_prompt
from core.models import UserMessage, AgentMessage, ToolCallMessage

AnyMessage: TypeAlias = Union[UserMessage, AgentMessage, ToolCallMessage]
MessageCallback: TypeAlias = Callable[[AnyMessage], None]

class ChatAgent:
    def __init__(self, model: BaseChatModel) -> None:
        self.model = model
        self.agent = create_agent(
            model=self.model,  # Default model
            tools=[],
            middleware=[handle_tool_errors],
            system_prompt=system_prompt
        )

    @staticmethod
    def _handle_message( message: Any, callback: MessageCallback) -> None:
        if message.content:
            if isinstance(message, HumanMessage):
                callback(
                    UserMessage(content=str(message.content)),
                )
            elif isinstance(message, AIMessage):
                callback(
                    AgentMessage(content=str(message.content)),
                )
        elif message.tool_calls:
            for tool_call in message.tool_calls:
                callback(
                    ToolCallMessage(
                        name=tool_call['name']
                    )
                )

    def stream(self, content: str, callback:MessageCallback ) -> None:
        for chunk in self.agent.stream({
            "messages": [HumanMessage(content=content)],
        }, stream_mode="values"):
            latest_message = chunk["messages"][-1]
            self._handle_message(latest_message, callback)
