from django.urls import path
from .views import MainForm


urlpatterns = [
    path('', MainForm.as_view()),
]
