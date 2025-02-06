import pytest
from app.services.chat_service import ChatService

def test_get_response():
    response = ChatService.get_response("Hello, how are you?")
    assert isinstance(response, str)