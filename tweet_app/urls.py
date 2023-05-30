from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "tweet_app"

urlpatterns = [
    path("",views.index,name="index"),
    path("add_tweet/",views.add_tweet,name="add_tweet"),
    path("list_tweet/",views.list_tweet,name="list_tweet"),
    path("signup/",views.SignUp.as_view(),name="signup"),
    path("delete_tweet/<int:id>",views.delete_tweet,name="delete_tweet")
    
]