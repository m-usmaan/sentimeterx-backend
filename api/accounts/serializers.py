from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.accounts.models import User

User = get_user_model()


class UserSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'id': instance.pk,
            'username': instance.username,
            'email': instance.email,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'full_name': instance.full_name,
            'avatar': instance.avatar.path if instance.avatar else None,
        }
