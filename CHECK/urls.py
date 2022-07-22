from django.urls import path
from CHECK import views
urlpatterns = [
    path('',views.CHECK),
    path('correct',views.CORRECT),
]