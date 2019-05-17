import json

from django.views.generic import TemplateView, View
from django.http import HttpResponse

from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters

from chat.models import Chat, TelegramUser, Message
from chat.serializers import MessageSerializer


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chats"] = Chat.objects.all()
        return context


class TelegramWebhookView(View):
    def post(self, request):
        payload = json.loads(request.body)
        message_data = payload.get("message", {})
        from_user_data = message_data.get("from")
        chat_data = message_data.get("chat")

        from_user, created = TelegramUser.objects.get_or_create(
            id=from_user_data["id"], defaults=dict(username=from_user_data["username"])
        )

        chat, created = Chat.objects.get_or_create(id=chat_data["id"])
        Message.objects.get_or_create(
            id=message_data["message_id"],
            defaults=dict(
                text=message_data.get("text", "****"),
                from_user=from_user,
                chat=chat,
                date_timestamp=message_data["date"],
            ),
        )

        return HttpResponse()


class RetrieveMessages(ListAPIView):
    serializer_class = MessageSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('chat_id',)
    queryset = Message.objects.all()
