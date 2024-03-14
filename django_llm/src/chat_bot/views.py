from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from chat_bot.models import Thread, Chat
import os
from datetime import datetime
import json

import openai

# Create your views here.
@login_required
def index(request):
    threads = Thread.objects.all()
    js_data = { "thread_id":0 }
    context = {"threads":threads, "js_data":json.dumps(js_data)}
    return render(request, "chat_bot/index.html", context)

@login_required
def chat(request, thread_id):
    threads = Thread.objects.all()
    now_thread = Thread.objects.get(id=thread_id)
    js_data = { "thread_id":now_thread.id }
    context = {"threads":threads, "now_thread":now_thread, "chats":now_thread.chats.all(), "js_data":json.dumps(js_data)}
    return render(request, "chat_bot/index.html", context)

openai.api_key = "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"
@api_view(["POST"])
def request_gpt(request, thread_id):
    if request.method == 'POST':
        message = request.data.get('message', '')

        # thread_id = request.data.get('thread_id', '')
        if not Thread.objects.filter(id=thread_id).exists():
            thread_id = add_thread(request.user)
        thread = Thread.objects.get(id=thread_id)
        
        add_chat(thread, message, request.user, request.user.username)

        messages = [{"role": "system", "content": "Assistant is a large language model trained by OpenAI."}]
        for chat in thread.chats.all():
            messages.append({"role": "user" if chat.name!="gpt" else "system", "content": chat.message})
        response = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            temperature = 0,
            messages = messages
        )
        generated_response = response.choices[0].message.content

        add_chat(thread, generated_response, request.user, "GPT")
        
        data = {'message': generated_response, 'thread_id':thread_id }
        return JsonResponse(data)
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Invalid HTTP method'})

def add_thread(user:User) -> int:
    thread = Thread(title="New", created_by=user)
    thread.save()
    return thread.id

def add_chat(thread:Thread, message:str, user:User, sender:str) -> None:
    chat = Chat(name=sender, message=message, thread=thread, created_by=user)
    chat.save()

@login_required
def delete_thread(request, thread_id):
    if not Thread.objects.filter(id=thread_id).exists(): return
    Thread.objects.delete(id=thread_id)
    return redirect("chat_bot/")

@login_required
def rename_thread(request, thread_id, name):
    if request.method == 'POST':
        if not Thread.objects.filter(id=thread_id).exists(): return
        thread = Thread.objects.get(id=thread_id)
        thread.title = name
        thread.save()
    else:
        return JsonResponse({'error': 'Invalid HTTP method'})