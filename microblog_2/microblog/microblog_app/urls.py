from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("post/", views.post, name="post"),
    path("post_form/", views.post_form, name="post_form"),
]
