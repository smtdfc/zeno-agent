from pydantic.dataclasses import dataclass


@dataclass
class UserMessage:
    content: str

@dataclass
class AgentMessage:
    content: str

@dataclass
class ToolCallMessage:
    name: str
