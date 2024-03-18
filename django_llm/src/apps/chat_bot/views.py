from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse, StreamingHttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Thread, Chat, GptSetting
from lib.gpt import models

import json
import openai


def index(request):
    threads = Thread.objects.filter(created_by=request.user)
    if not GptSetting.objects.filter(created_by=request.user).exists():
        gpt_setting = GptSetting(created_by = request.user)
        gpt_setting.save()
    gpt_setting = GptSetting.objects.get(created_by=request.user)
    js_data = { "thread_id":0 }
    context = {"threads":threads, "models":models.get_models(), "gpt_setting":gpt_setting, "js_data":json.dumps(js_data)}
    return render(request, "chat_bot/index.html", context)

def chat(request, thread_id):
    threads = Thread.objects.filter(created_by=request.user)
    if not GptSetting.objects.filter(created_by=request.user).exists():
        gpt_setting = GptSetting(created_by = request.user)
        gpt_setting.save()
    gpt_setting = GptSetting.objects.get(created_by=request.user)
    now_thread = Thread.objects.get(id=thread_id)
    js_data = { "thread_id":now_thread.id }
    context = {"threads":threads, "models":models.get_models(), "gpt_setting":gpt_setting, "now_thread":now_thread, "chats":now_thread.chats.all(), "js_data":json.dumps(js_data)}
    return render(request, "chat_bot/index.html", context)

openai.api_key = "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"
class ChatGPTStreamView(APIView):
    def post(self, request, thread_id):
        message = request.data.get('message', '')
        model = request.data.get('model', '')
        temperature = request.data.get('temperature', '')

        gptSetting = GptSetting.objects.get(created_by = request.user)
        gptSetting.model = model
        gptSetting.temperature = float(temperature)
        gptSetting.save()

        thread = Thread.objects.get(id=thread_id)

        messages = [{"role": "user" if chat.sender!="gpt" else "system", "content": chat.message} for chat in thread.chats.all()]
        messages.append({"role": "user", "content": message})

        response = openai.chat.completions.create(model=gptSetting.model, messages=messages, temperature=gptSetting.temperature, stream=True)

        def generate_stream_response():
            for chunk in response:
                text = chunk.choices[0].delta.content
                yield text

        return StreamingHttpResponse(generate_stream_response(), content_type="text/plain")


def delete_thread(request, thread_id):
    if not Thread.objects.filter(id=thread_id).exists(): return
    thread = Thread.objects.get(id=thread_id)
    thread.delete()
    return redirect("chat_bot:chat_bot")

def rename_thread(request, thread_id):
    if not Thread.objects.filter(id=thread_id).exists(): return
    thread = Thread.objects.get(id=thread_id)
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    thread.title = body_data.get('name', None)
    thread.save()
    return redirect("chat_bot:chat_bot")

def add_thread(user:User) -> int:
    thread = Thread(title="New", created_by=user)
    thread.save()
    return thread.id

def add_chat(thread:Thread, message:str, user:User, sender:str) -> None:
    chat = Chat(sender=sender, message=message, thread=thread, created_by=user)
    chat.save()

@api_view(["POST"])
def add_new_thread(request):
    thread = Thread(title="New", created_by=request.user)
    thread.save()
    return JsonResponse({"thread_id":thread.id})

@api_view(["POST"])
def add_chat_history(request, thread_id):
    user_message = request.data.get('user_message', '')
    gpt_message = request.data.get('gpt_message', '')
    thread = Thread.objects.get(id=thread_id)
    add_chat(thread=thread, message=user_message, user=request.user, sender=request.user.username)
    add_chat(thread=thread, message=gpt_message, user=request.user, sender="GPT")
    return JsonResponse({"thread_id":thread.id})
