from rest_framework import serializers

from api.chats.models import Chat
from utils import get_datetime_breakdown
from utils.fields import DateTimeBreakdownField


class ChatsListSerializer(serializers.BaseSerializer):
    def to_representation(self, instance: Chat):
        return {
            'unique_uuid': instance.unique_uuid,
            'user_query': instance.user_query,
            'is_pinned': instance.is_pinned,
            'created_at': get_datetime_breakdown(instance.created_at)
        }


class ChatDetailSerializer(serializers.BaseSerializer):
    def to_representation(self, instance: Chat):
        return {
            'unique_uuid': instance.unique_uuid,
            'user_query': instance.user_query,
            'is_pinned': instance.is_pinned,
            'created_at': get_datetime_breakdown(instance.created_at),
            'summary': instance.summary,
            'detailed_analysis': instance.detailed_analysis,
            'visualization': instance.visualization,
            'feedback_quotes': instance.feedback_quotes
        }


class ChatCreateSerializer(serializers.ModelSerializer):
    created_at = DateTimeBreakdownField(read_only=True)
    class Meta:
        model = Chat
        fields = '__all__'
        read_only_fields = [
            'unique_uuid', 'is_pinned', 'created_at', 'summary', 'detailed_analysis', 'visualization', 'feedback_quotes'
        ]
        extra_kwargs = {
            'user': {'required': True, 'write_only': True},
        }
    
    def to_internal_value(self, data):
        data['user'] = self.context['request'].user.pk
        return super().to_internal_value(data)
