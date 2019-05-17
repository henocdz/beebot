"""beebot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from chat.views import (
    HomeView,
    TelegramWebhookView,
    RetrieveMessagesView,
    SendMessageView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view()),
    path("webhooks/telegram/", csrf_exempt(TelegramWebhookView.as_view())),
    path("api/messages/", RetrieveMessagesView.as_view()),
    path("api/messages/send/", SendMessageView.as_view()),
]
