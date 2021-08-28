from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title")

    # create a new page section

    # create an edit page section
]
