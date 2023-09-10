from enum import Enum


class EventType(Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"


class ResourceType(Enum):
    MESSAGE = "message"
    ORGANIZATION = "organization"
    ROLE = "role"
    THREAD = "thread"
    USER = "user"


class MessageType(Enum):
    TEXT = "text"
    IMAGE = "image"
