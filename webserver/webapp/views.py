import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Count
from .models import Topic, TopicForm, Reply, ReplyForm


def index(request):
    return HttpResponse("ParkC Django WebApp")


def ping(request):
    return HttpResponse("pong")


def topics(request):
    topics = Topic.objects.annotate(
        reply_count=Count("reply")).order_by("topic_id")
    return render(request, "topics.html", {"topics": topics})


def register(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.topic_id = str(round(time.time()*1000))
            new_topic.save()
            return HttpResponseRedirect("/topics")
    else:
        form = TopicForm()
    return render(request, "register.html", {"form": form})


def view(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    replies = Reply.objects.filter(topic_id=topic_id).order_by("reply_id")
    return render(request, "topic.html", {"topic": topic, "replies": replies})


def edit(request, topic_id):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.topic_id = topic_id
            new_topic.save()
            return HttpResponseRedirect("/topics")
    else:
        form = TopicForm()
    topic = Topic.objects.get(pk=topic_id)
    return render(request, "edit.html", {"topic": topic})


def reply(request, topic_id):
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.reply_id = str(round(time.time()*1000))
            new_reply.topic_id = Topic.objects.get(pk=topic_id)
            new_reply.save()
    else:
        form = ReplyForm()
    return HttpResponseRedirect(f'/topics/{topic_id}')


def delete_topic(request, topic_id):
    Topic.objects.filter(pk=topic_id).delete()
    return HttpResponseRedirect("/topics")


def delete_reply(request, topic_id, reply_id):
    Reply.objects.filter(pk=reply_id).delete()
    return HttpResponseRedirect(f'/topics/{topic_id}')
