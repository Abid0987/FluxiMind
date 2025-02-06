from flask import Blueprint, request, jsonify
from app.services.chat_service import ChatService

# Create a Blueprint for chat routes
chat_routes = Blueprint("chat_routes", __name__)

@chat_routes.route("/chat", methods=["POST"])
def chat():
    """
    Handles POST requests to the /chat endpoint.
    """
    user_input = request.json.get("message")
    response = ChatService.get_response(user_input)
    return jsonify({"response": response})