from rest_framework import serializers
from datetime import datetime
from utils import get_datetime_breakdown


class DateTimeBreakdownField(serializers.DateTimeField):
    def to_representation(self, value: datetime):
        return get_datetime_breakdown(value)

    def to_internal_value(self, data):
        raise NotImplementedError("This field is read-only.")
