from django.urls import path
from .views import ContentInput

urlpatterns = (
    path('api/', ContentInput.as_view()),
)