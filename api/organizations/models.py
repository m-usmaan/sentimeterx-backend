from django.db import models
from django.db.models.functions import Lower
from simple_history.models import HistoricalRecords


class Organization(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=35, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()


    class Meta:
        db_table = 'organizations'
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='name_case_insensitive_unique',
                violation_error_message='Name already exists'
            ),
            models.UniqueConstraint(
                Lower('slug'),
                name='slug_case_insensitive_unique',
                violation_error_message='Slug already exists'
            )
        ]
    
    def __str__(self):
        return self.slug