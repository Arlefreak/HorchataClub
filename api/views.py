from api.models                    import *
from api.serializers               import *
from rest_framework                import permissions
from rest_framework                import viewsets
from rest_framework                import filters
from taggit.models                 import Tag
from taggit_serializer.serializers import TaggitSerializer

class HorchataViewSet(viewsets.ModelViewSet):
        queryset           = Horchata.objects.all()
        serializer_class   = HorchataSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filter_fields = ('slug','price')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
