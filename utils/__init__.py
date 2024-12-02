from rest_framework.exceptions import ParseError


def get_param(params, key, data_type, default=None):
    """Method to get parameter from a dictionary"""
    try:
        return data_type(params.get(key)) if params.get(key) else default
    except ValueError:
        raise ParseError
