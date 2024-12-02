from rest_framework.generics import ListAPIView
from api.chats.models import Chat
from api.chats.serializers import ChatsListSerializer


class ChatsListAPIView(ListAPIView):
    serializer_class = ChatsListSerializer

    def get_queryset(self):
        return Chat.objects.filter(user=self.request.user)
