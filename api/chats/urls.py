from rest_framework.routers import DefaultRouter
from api.chats.views import ChatAPIViewSet

router = DefaultRouter()
router.register('', ChatAPIViewSet, basename='chat')

urlpatterns = router.urls