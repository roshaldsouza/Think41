# chat/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ChatMessage

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        msg = ChatMessage(
            username=data.get('username'),
            message=data.get('message')
        )
        msg.save()
        return JsonResponse({'status': 'Message saved'}, status=201)
    
    elif request.method == 'GET':
        messages = ChatMessage.objects.order_by('-timestamp')[:50]
        data = [
            {"username": m.username, "message": m.message, "timestamp": m.timestamp.isoformat()}
            for m in messages
        ]
        return JsonResponse(data, safe=False)
