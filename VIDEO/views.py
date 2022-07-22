from django.shortcuts import render, redirect
from django.http import HttpResponse
from matplotlib.pyplot import title
from django.apps import apps
from .models import *
from ERUDITION.views import user_info

# Create your views here.
tables = apps.get_app_config("VIDEO")
all_=[]
for i in tables.models.values():
    all_.append(i)
main_topic = all_[1]

def VIDEO(request):
    global main_topic
    topic = Topic.objects.all()
    Videos,video = main_topic.objects.all(), main_topic.objects.filter()[:1].get()
    if request.user.is_anonymous:
        return redirect('/signin')
    if request.POST.get("sub-topic"):
        if request.method=="POST":
            sub_topic=request.POST.get("sub-topic")
            video=main_topic.objects.get(title=sub_topic)
    else:
        if request.method=="POST":
            main_topic=request.POST.get("main-topic")
            for a in all_:
                temp = str(a)
                temp1 = "<class 'VIDEO.models."+main_topic+"'>"
                if temp==temp1:
                    main_topic=a
                    break
            Videos,video=main_topic.objects.all(), main_topic.objects.filter()[:1].get()
    
    details={"Videos":Videos, "video":video, "Topics":topic}
    details.update(user_info(request))
    return render(request, 'VIDEO/VIDEO.html',details)