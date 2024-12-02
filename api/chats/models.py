import uuid
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Chat(models.Model):
    unique_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")
    created_at = models.DateTimeField(auto_now_add=True)
    summary = models.JSONField(blank=True, null=True)
    detailed_analysis = models.JSONField(blank=True, null=True)
    visualization = models.JSONField(blank=True, null=True)
    feedback_quotes = models.JSONField(blank=True, null=True)
    is_pinned = models.BooleanField(default=False)

    class Meta:
        db_table = 'chats'
        constraints = [
            models.UniqueConstraint(fields=['user', 'unique_uuid'], name='unique_chat_id_per_user')
        ]

    def __str__(self):
        return f"Chat {self.unique_uuid} for {self.user.username}"
