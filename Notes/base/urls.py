
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('add/',views.addNotes, name="addn"),
    path('delete<str:q>/',views.deleteNote,name="delete"),
]