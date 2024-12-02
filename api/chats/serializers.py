from rest_framework import serializers

from api.chats.models import Chat


class ChatsListSerializer(serializers.BaseSerializer):
    def to_representation(self, instance: Chat):
        created_at = instance.created_at
        return {
            'id': instance.unique_uuid,
            'user_query': instance.user_query,
            'is_pinned': instance.is_pinned,
            'created_at': {
                'year': created_at.year,
                'month': created_at.month,
                'day': created_at.day,
                'hour': created_at.hour,
                'minute': created_at.minute,
                'second': created_at.second,
            }
        }
