from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    # path("<int:pk>/", views.project_detial, name="project_detial"),
]
