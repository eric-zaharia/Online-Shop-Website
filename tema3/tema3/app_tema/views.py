import datetime

import form as form
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Post, Comment


def hello(request):
    return HttpResponse('Buna ziua!')


def home(request):
    context = {
        'nr': 1234,
    }
    return render(request, 'home.html', context=context)


class TabeleView(View):
    @classmethod
    def get(cls, request):
        posts = Post.objects.all().order_by('-data_p')

        context = {
            'posts': posts,
        }

        return render(request, 'tabele.html', context=context)

    @classmethod
    def post(cls, request):
        if request.POST['tipform'] == 'post':

            Post(
                titlu=request.POST['titlu'],
                data_p=datetime.datetime.now(),
                autor=request.POST['autor'],
                continut=request.POST['continut'],
            ).save()

        elif request.POST['tipform'] == 'comment':

            post = Post.objects.get(id=request.POST['post'])

            Comment(
                post=post,
                nume_cont=request.POST['nume_cont'],
                continut=request.POST['continut_com'],
                data_ora=datetime.datetime.now(),
            ).save()

        return HttpResponseRedirect(reverse('my_app:tabele'))

