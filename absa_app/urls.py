from django.urls import path

from .views import *

urlpatterns = [
	path('', HomeView.as_view(), name="home"),
    path('technical-notes/', TechnicalNotes.as_view(), name="technical-notes")
]
