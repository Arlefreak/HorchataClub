from api.models                    import Horchata
from api.serializers               import HorchataSerializer, UserSerializer
from django.contrib.auth.models    import User
from rest_framework                import permissions
from rest_framework                import viewsets
from rest_framework                import filters
from rest_framework                import response

# from taggit.models                 import Tag

class HorchataViewSet(viewsets.ModelViewSet):
        queryset           = Horchata.objects.filter(publish=True)
        serializer_class   = HorchataSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filter_fields = ('slug', 'publish')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return response.Response(UserSerializer(request.user,
                context={'request':request}).data)
        return super(UserViewSet, self).retrieve(request, pk)
