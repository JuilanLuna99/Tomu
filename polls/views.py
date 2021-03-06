from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser, User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from django.core import serializers
from .models import *
import datetime
import re
import json
# Create your views here.

def polls(request):
    polls=Poll.objects.all().order_by("-created")
    return render(request, "polls.html", {"polls": polls})

def getPoll(request, id):
    poll = Poll.objects.filter(id=id).first()
    data = {
        "id": poll.id,
        "columns": [[x.choice, x.voted()] for x in poll.allChoices()],
    }

    return HttpResponse(json.dumps(data), content_type='application/json')

def makePoll(request):
    if request.method == 'POST':
        title = request.POST['Title']
        closetime = datetime.now() + datetime.timedelta(hours=request.POST['hours'])
        answers = []
        for a in request.POST.keys():
            if re.search(r'^a(\d+)', a) != None:
                answers.append(request.POST[a])
        if len(answers) <= 1:
            return HttpResponse(status=400)

        poll = Poll(name=title, closetime=closetime, admin=request.user)
        poll.save()
        for i in range(len(answers)):
            choice = Choice(choice=answers[i], poll=poll, idinPoll=i)
            choice.save()

        return redirect("polls")
    return redirect("polls")

def vote(request, poll_id):
    if request.method == 'POST':
        pass
    else:
        return HttpResponseRedirect("polls")
