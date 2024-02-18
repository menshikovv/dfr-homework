from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .permissions import IsAdvertisementCreator
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdvertisementCreator]
    filterset_class = AdvertisementFilter