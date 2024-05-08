from django.urls import path
from . import views
urlpatterns = [
    path('snplus/create/', views.create_snplus)
]
