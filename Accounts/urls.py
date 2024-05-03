from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('<int:user_id>/', views.AccountMangement.as_view()),
]
