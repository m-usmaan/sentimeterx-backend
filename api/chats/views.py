from rest_framework.generics import ListAPIView
from api.chats.models import Chat
from api.chats.serializers import ChatsListSerializer
from utils import get_param


class ChatsListAPIView(ListAPIView):
    serializer_class = ChatsListSerializer

    def get_queryset(self):
        query = {
            'user': self.request.user
        }
        pinned = get_param(self.request.query_params, 'pinned', str, '').lower()
        if pinned and pinned in ['true', 'false']:
            query['is_pinned'] = pinned == 'true'

        return Chat.objects.filter(**query)
