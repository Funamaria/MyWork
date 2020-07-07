from django.urls import path
from .views import ContentInput, GoodsGet

urlpatterns = (
    path('api/', ContentInput.as_view()),
    path('apic/', GoodsGet.as_view()),
)