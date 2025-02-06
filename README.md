# **The FluxiMind Project**

A Flask-based AI system that integrates with the **DeepSeek API** to provide a chatbot interface. This project includes a backend for handling API requests and a simple frontend for user interaction.

---

## **Table of Contents**
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
4. [Running the Application](#running-the-application)
5. [Folder Structure](#folder-structure)
6. [API Documentation](#api-documentation)
7. [Testing](#testing)
8. [Troubleshooting](#troubleshooting)
9. [Contributing](#contributing)
10. [License](#license)

---

## **Features**
- **Chatbot Interface**: Interact with the DeepSeek AI through a simple web interface.
- **Modular Code**: Clean and organized codebase with separate modules for API, services, and routes.
- **Scalable**: Easily extendable to add more features like user authentication, database integration, etc.

---

## **Prerequisites**
Before running the project, ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- **DeepSeek API Key** (Get it from [DeepSeek](https://www.deepseek.com))

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/deepseek-ai-project.git
cd deepseek-ai-project
```

### **2. Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**
Create a `.env` file in the root directory and add your DeepSeek API key:
```plaintext
DEEPSEEK_API_KEY=your_api_key_here
```

---

## **Running the Application**

### **1. Start the Backend**
Run the Flask backend:
```bash
python main.py
```
The backend will start at `http://127.0.0.1:5000`.

### **2. Open the Frontend**
Open the `frontend/index.html` file in your browser to interact with the chatbot.

---

## **Folder Structure**
```
deepseek-ai-project/
│
├── .env/                     # Environment variables (e.g., API keys)
├── .gitignore                # Files/folders to ignore in Git
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
│
├── app/                      # Main application code
│   ├── __init__.py           # Initialize the app
│   ├── api/                  # API-related code
│   │   ├── __init__.py
│   │   └── deepseek_api.py   # DeepSeek API wrapper
│   ├── services/             # Business logic
│   │   ├── __init__.py
│   │   └── chat_service.py   # Chatbot service
│   ├── routes/               # API routes (for Flask)
│   │   ├── __init__.py
│   │   └── chat_routes.py    # Chatbot API endpoints
│   └── config.py             # Configuration settings
│
├── tests/                    # Unit and integration tests
│   ├── __init__.py
│   ├── test_api.py           # Test DeepSeek API wrapper
│   └── test_chat_service.py  # Test chatbot service
│
├── frontend/                 # Frontend code
│   ├── index.html            # HTML file for the chatbot UI
│   ├── styles.css            # CSS for styling
│   └── script.js             # JavaScript for interactivity
│
├── logs/                     # Log files
│   └── app.log               # Application logs
│
└── main.py                   # Entry point for the application
```

---

## **API Documentation**

### **Chat Endpoint**
- **URL**: `/chat`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "message": "Hello, how are you?"
  }
  ```
- **Response**:
  ```json
  {
    "response": "I'm just a computer program, so I don't have feelings, but I'm here to help! How can I assist you today?"
  }
  ```

---

## **Testing**
Run the unit tests to ensure the application works as expected:
```bash
python -m pytest tests/
```

---

## **Troubleshooting**
If the AI is not responding:
1. Verify that the `.env` file contains the correct API key.
2. Check the Flask logs for errors.
3. Test the backend API using **curl** or **Postman**:
   ```bash
   curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "Hello, how are you?"}'
   ```

---

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

### Find Me on:
<p align="left">
  <a href="https://github.com/Abid0987" target="_blank"><img src="https://img.shields.io/badge/Github-blue?style=for-the-badge&logo=github"></a>
  <a href="https://www.hackerrank.com/mdabid224499" target="_blank"><img src="https://img.shields.io/badge/hackerrank-black?style=for-the-badge&logo=hackerrank"></a>
  <a href="https://leetcode.com/black_hate/" target="_blank"><img src="https://img.shields.io/badge/leetcode-black?style=for-the-badge&logo=leetcode"></a>
  <a href="https://www.linkedin.com/in/abid-hasan-99345b26a/" target="_blank"><img src="https://img.shields.io/badge/linkedin-blue?style=for-the-badge&logo=linkedin"></a>
</p>

---

Enjoy building and using your DeepSeek AI system! 🚀
