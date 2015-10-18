
from rest_framework                import serializers
from django.contrib.auth.models    import User
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from api.models                    import *
from taggit.models                 import Tag

class HorchataSerializer(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    class Meta:
        model = Horchata
