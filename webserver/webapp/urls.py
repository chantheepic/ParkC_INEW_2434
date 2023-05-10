from django.urls import path

from . import views
from webapp.views import index, topics, register, view, edit, reply, delete_topic, delete_reply

urlpatterns = [
    path("register", register),
    path("<slug:topic_id>", view),
    path("<slug:topic_id>/edit", edit),
    path("<slug:topic_id>/reply", reply),
    path("<slug:topic_id>/delete", delete_topic),
    path("<slug:topic_id>/reply/<slug:reply_id>/delete", delete_reply),
    path("", topics)
]
