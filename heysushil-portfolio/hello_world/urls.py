# path ko import kiye hai url access ke liye
from django.urls import path
# isko add kiya hai controller methods or class ka access dene ke liye
from hello_world import views

urlpatterns = [
    path('',views.hello_world, name='hello_world'),
]


