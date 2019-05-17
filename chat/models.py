from django.db import models

# Create your models here.


class Chat(models.Model):
    id = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return self.username


class TelegramUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    from_user = models.ForeignKey("chat.TelegramUser", on_delete=models.PROTECT)
    chat = models.ForeignKey("chat.Chat", on_delete=models.PROTECT)
    date_timestamp = models.IntegerField()

    def __str__(self):
        return f"{self.from_user.username}: {self.text}"
