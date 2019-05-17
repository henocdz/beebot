from django.contrib import admin

from chat.models import Chat, TelegramUser, Message

admin.site.register([Chat, TelegramUser, Message])
