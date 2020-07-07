from django.urls import path
from .views import ContentInput, GoodsGet

urlpatterns = (
    path('content/', ContentInput.as_view()),
    path('goods/', GoodsGet.as_view()),
)