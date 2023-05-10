from django.db import models
from django import forms


class Topic(models.Model):
    topic_id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["title", "content", "author"]


class Reply(models.Model):
    reply_id = models.CharField(max_length=50, primary_key=True)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    reply = models.TextField()
    author = models.CharField(max_length=100)


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["reply", "author"]
