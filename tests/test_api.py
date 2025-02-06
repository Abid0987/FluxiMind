import pytest
from app.api.deepseek_api import send_to_deepseek

def test_send_to_deepseek():
    response = send_to_deepseek("Hello, how are you?")
    assert isinstance(response, str)