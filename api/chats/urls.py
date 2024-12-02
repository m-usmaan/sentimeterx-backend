from django.urls import path
from api.chats.views import ChatsListAPIView

urlpatterns = [
     path('all', ChatsListAPIView.as_view(), name='all_chats'),
]