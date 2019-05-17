from rest_framework import serializers
from chat.models import Message, TelegramUser


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    from_user = TelegramUserSerializer()

    class Meta:
        model = Message
        fields = "__all__"


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["chat", "text"]
