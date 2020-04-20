from django.urls import path
from . import views

urlpatterns = [
    path('ImageUpload/', views.image_upload),
]
