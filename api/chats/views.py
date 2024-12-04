from api.chats.models import Chat
from api.chats.serializers import ChatsListSerializer, ChatDetailSerializer, ChatCreateSerializer
from utils import get_param
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status


class ChatAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'delete']  # Only allow these methods

    def get_serializer_class(self):
        serializer_classes = {
            'retrieve': ChatDetailSerializer,
            'create': ChatCreateSerializer,
            'list': ChatsListSerializer
        }
        return serializer_classes.get(self.action)
    
    def get_queryset(self):
        query = {'user': self.request.user}
        if self.action == 'list':
            pinned = get_param(self.request.query_params, 'pinned', str, '').lower()
            if pinned in ['true', 'false']:
                query['is_pinned'] = pinned == 'true'

        return Chat.objects.filter(**query)
    
    @action(detail=True, methods=['get'], url_name='chat-summary')
    def summary(self, request, pk=None):
        return self._get_field('summary')
    
    @action(detail=True, methods=['get'], url_name='chat-detailed-analysis', url_path='detailed-analysis')
    def detailed_analysis(self, request, pk=None):
        return self._get_field('detailed_analysis')
    
    @action(detail=True, methods=['get'], url_name='chat-visualization')
    def visualization(self, request, pk=None):
        return self._get_field('visualization')
    
    @action(detail=True, methods=['get'], url_name='chat-feedback-quotes', url_path='feedback-quotes')
    def feedback_quotes(self, request, pk=None):
        return self._get_field('feedback_quotes')
    
    @action(detail=True, methods=['get'], url_name='chat-toggle-pin', url_path='toggle-pinned')
    def toggle_is_pinned(self, request, pk=None):
        chat: Chat = self.get_object()
        chat.is_pinned = not chat.is_pinned
        chat.save(update_fields=['is_pinned'])
        return Response({'is_pinned': chat.is_pinned}, status=status.HTTP_200_OK)
    
    def _get_field(self, field: str):
        chat: Chat = self.get_object()
        data = getattr(chat, field)  # Make call to techtics API if field is null
        return Response({field: data}, status=status.HTTP_200_OK)
