# chat/models.py
from mongoengine import Document, StringField, DateTimeField
import datetime

class ChatMessage(Document):
    username = StringField(required=True)
    message = StringField(required=True)
    timestamp = DateTimeField(default=datetime.datetime.utcnow)
