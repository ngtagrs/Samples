from django.contrib import admin
from .models import Thread, Chat, GptSetting

admin.site.register(Thread)
admin.site.register(Chat)
admin.site.register(GptSetting)