from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("create/",views.create,name="create"),
    path("results/<int:poll_id>/",views.results,name="results"),
    path("vote/<int:poll_id>/",views.vote,name="vote"),
]