from app.api.deepseek_api import send_to_deepseek

class ChatService:
    @staticmethod
    def get_response(user_input):
        """
        Gets a response from the DeepSeek API.
        """
        return send_to_deepseek(user_input)