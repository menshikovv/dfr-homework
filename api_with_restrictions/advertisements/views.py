from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .permissions import IsAdvertisementCreator
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = AdvertisementFilter

    def perform_update(self, serializer):
        """Проверка на автора при обновлении объявления."""
        if serializer.instance.creator == self.request.user:
            serializer.save()
        else:
            raise PermissionError("Вы не являетесь автором этого объявления.")

    def perform_destroy(self, instance):
        """Проверка на автора при удалении объявления."""
        if instance.creator == self.request.user:
            instance.delete()
        else:
            raise PermissionError("Вы не являетесь автором этого объявления.")
