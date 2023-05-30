from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.urls import reverse ,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView



# Create your views here.

def index(request):
    return render(request,"tweet_app/index.html")

@login_required(login_url="/login")
def add_tweet(request):
    if request.POST:
        message = request.POST["message"]
        models.Tweet_user.objects.create(nick = request.user  , message=message)
        return redirect(reverse("tweet_app:list_tweet"))
    return render(request,'tweet_app/add_tweet.html')
        
def list_tweet(request):
    all_tweets = models.Tweet_user.objects.all()
    tweet_dict = {"tweets":all_tweets}
    return render(request,"tweet_app/list_tweet.html", context=tweet_dict)

@login_required
def delete_tweet(request,id):
    tweet = models.Tweet_user.objects.get(pk = id)
    if request.user == tweet.nick: 
        models.Tweet_user.objects.filter(id=id).delete()
        return redirect("tweet_app:list_tweet")
    


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
