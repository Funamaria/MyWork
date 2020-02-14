from rest_framework import viewsets, routers
from mysite.models import Content
from mysite.serializers import CntentSerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

router = routers.DefaultRouter()
router.register(r'content', ContentViewSet)