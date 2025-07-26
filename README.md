# 🧠 Chat API with LLM Integration using Django + MongoDB

This project implements a core chat backend using Django, MongoDB, and Large Language Models (LLMs). It features REST APIs for user-agent chat, stores conversations in MongoDB using `mongoengine`, and integrates with an LLM (e.g., Groq) to generate responses.

---

## 🚀 Features

- 🔧 RESTful `/api/chat/` endpoint to handle chat messages
- 💾 Persistence of conversations in MongoDB
- 🧠 Integration with an LLM to generate intelligent replies
- 📄 Uses `mongoengine` as the ORM to connect Django with MongoDB

---

## 🔧 Tech Stack

- **Backend:** Django (DRF)
- **Database:** MongoDB (via `mongoengine`)
- **AI Integration:** Groq API (or any OpenAI-compatible LLM)
- **Python Version:** 3.10+

---

## 📁 Project Structure

chatbot/
├── chatbot/ # Main Django project
│ ├── settings.py
│ ├── urls.py
├── api/ # Chat API app
│ ├── models.py # MongoEngine models
│ ├── views.py # Chat logic + LLM integration
│ ├── urls.py
├── requirements.txt

yaml
Copy
Edit

---

## 🧪 API Endpoint

### `POST /api/chat/`

**Request JSON:**
```json
{
  "message": "Hello, what can you do?",
  "conversation_id": "optional-convo-id"
}
Response:

json
Copy
Edit
{
  "conversation_id": "abc123",
  "user_message": "Hello, what can you do?",
  "ai_response": "I'm an AI assistant. How can I help you today?"
}
⚙️ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/chat-api-llm.git
cd chat-api-llm
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Configure MongoDB in settings.py
python
Copy
Edit
from mongoengine import connect
connect(
    db='chat_db',
    host='mongodb://localhost:27017/chat_db',
)
4. Set up Groq API Key
Create a .env file:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
Load it in your view using:

python
Copy
Edit
import os
from dotenv import load_dotenv
load_dotenv()
5. Run server
bash
Copy
Edit
python manage.py runserver
