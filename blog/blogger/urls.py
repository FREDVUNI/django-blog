from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path('list',views.listblog,name="list"),
    path("create",views.create,name="create"),
    path("about-us",views.about,name="about"),
    path("contact-us",views.contact,name="contact"),
    path("<str:slug>",views.details,name="details"),
    path("<str:slug>/edit",views.update,name="update"),
    path("<str:slug>/delete",views.delete,name="delete"),

]