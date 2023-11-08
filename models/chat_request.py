
from pydantic import BaseModel

class ChatMessage(BaseModel):
    def __init__(self, message: str, sender: str):
        self.message = message
        self.sender = sender
        
class ChatRequest(BaseModel):
    messages: list[ChatMessage] 
