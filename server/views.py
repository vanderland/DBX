from django.shortcuts import render
from django.views import generic
from .models import Server


class ServerView(generic.ListView):
    template_name = 'server/index.html'
    context_object_name = 'server_list'

    def get_queryset(self):
        return Server.objects.all()

