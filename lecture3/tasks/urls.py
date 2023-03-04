from django.urls import path
from . import views

app_name = "tasks"
# to avoid namespace collision
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
