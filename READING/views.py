from django.shortcuts import render, redirect
from ERUDITION.views import user_info
from django.http import HttpResponse
from .models import *
# Create your views here.
def INDEX(request):
    topic = Topic.objects.all()
    subtopic = SubTopic.objects.all()
    details = {"Topics":topic, "SubTopics":subtopic, "SubTopicsLen":len(subtopic)+1}
    if request.user.is_anonymous:
        return redirect('/signin')
    details.update(user_info(request))
    return render(request, "READING/INDEX.html", details)

def main(request):
    cur_topic=request.POST.get("cur-topic")
    topic, subtopic, allsubtopic = Topic.objects.all(), SubTopic.objects.filter(stopic_id = cur_topic), SubTopic.objects.all()
    details = {"Topics":topic, "SubTopics":subtopic, "Val":len(subtopic), "AllSubTopics":allsubtopic}
    details.update(user_info(request))
    return details

# ARTICLES

def A(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request, "READING/A.html", main(request))
def AN(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request, "READING/AN.html", main(request))
def THE(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request, "READING/THE.html", main(request))

# PARTS OF SPEECH

def NOUN(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request, "READING/NOUN.html", main(request))

def PRONOUN(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request, "READING/PRONOUN.html", main(request))

def VERB(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request, "READING/VERB.html", main(request))
    
def ADJECTIVE(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request, "READING/ADJECTIVE.html", main(request))

def ADVERB(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request, "READING/ADVERB.html", main(request))

def PREPOSITION(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request, "READING/PREPOSITION.html", main(request))

def CONJUNCTION(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request, "READING/CONJUNCTION.html", main(request))

def INTERJECTION(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request, "READING/INTERJECTION.html", main(request))
