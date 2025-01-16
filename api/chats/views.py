from api.chats.models import Chat
from api.chats.serializers import ChatsListSerializer, ChatDetailSerializer, ChatCreateSerializer
from utils import get_param
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from services.techtics import TechticsClient


client = TechticsClient()


class ChatAPIViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'delete']  # Only allow these methods
    _field_callback = {
        'summary': client.get_summary,
        'detailed_analysis': client.get_analysis,
        'visualization': client.get_visualization,
        'feedback_quotes': client.get_feedback_quotes
    }

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

        return Chat.objects.filter(**query).order_by('-created_at')

    @action(detail=False, methods=['get'], url_path='suggestions')
    def chat_suggestions(self, request):
        return Response(client.get_chat_suggestions(), status=status.HTTP_200_OK)

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
        data = getattr(chat, field)
        if not data:
            callback = self._field_callback.get(field)
            kwargs = {'chat_id': chat.unique_uuid}
            if field == 'summary':
                kwargs['user_query'] = chat.user_query
            data = callback(**kwargs) if callback else None
            setattr(chat, field, data)
            chat.save()

        return Response({field: data}, status=status.HTTP_200_OK)


class DataSetsAPIView(APIView):
    http_method_names = ['get']

    def get(self, request):
        return Response(client.get_data_sets(), status=status.HTTP_200_OK)


class DatasetFiltersView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        dataset_id = kwargs['dataset_id']
        return Response(client.get_filters(dataset_id), status=status.HTTP_200_OK)
