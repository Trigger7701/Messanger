from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import json
def messanger(request):
    profiles = Profiles.objects.all()
    context = {
        'profiles':profiles
    }
    return render(request,'messaging.html',context)
def chat(request):
    data = json.loads(request.body)
    print(data)
    reciver = Profiles.objects.get(id=data['reciver_id'])
    sender = Profiles.objects.get(user=request.user)
    chat = get_chat(sender,reciver)
    try:
        messages = Messages.objects.filter(chat=chat)

    except:
        messages = []
    res = []

    for message in messages:
        d = {
            'sender':message.sender.id,
            'text':message.text,
            'time':message.mtime
        }
        res.append(d)
    users = {
        'sender':{
            'username':sender.user.username,
            'image':sender.imageURL
        },
        'reciver':{
            'username': reciver.user.username,
            'image': reciver.imageURL
        }
    }
    print(res)
    return JsonResponse({'messages':res,'users':users})
def sendmessage(request):
    data = json.loads(request.body)
    reciver = Profiles.objects.get(id=data['reciver_id'])
    sender = Profiles.objects.get(user=request.user)
    chat = get_chat(sender,reciver)
    message = Messages.objects.create(chat=chat,sender=sender,text=data['message'])
    message.save()
    return JsonResponse({'time':message.mtime,'status':200})
def get_chat(s,r):
    chats = Chats.objects.filter(user1=r).filter(user2=s) | Chats.objects.filter(user2=r).filter(
        user1=s)
    if chats:
        chat = chats[0]
    else:
        chat, created = Chats.objects.get_or_create(user1=s, user2=r)
    return chat