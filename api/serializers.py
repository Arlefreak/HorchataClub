from rest_framework                import serializers
from django.contrib.auth.models    import User
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from api.models                    import Horchata

class HorchataSerializer(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    class Meta:
        model = Horchata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
