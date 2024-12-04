from rest_framework.exceptions import ParseError
from datetime import datetime


def get_param(params, key, data_type, default=None):
    """Method to get parameter from a dictionary"""
    try:
        return data_type(params.get(key)) if params.get(key) else default
    except ValueError:
        raise ParseError


def get_datetime_breakdown(value: datetime) -> dict:
    return {
        'year': value.year,
        'month': value.month,
        'day': value.day,
        'hour': value.hour,
        'minute': value.minute,
        'second': value.second,
        'timezone': str(value.tzinfo)
    }
