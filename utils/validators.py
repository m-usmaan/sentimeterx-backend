from django.core import validators


class CustomUsernameValidator(validators.RegexValidator):
    regex = '^[\w._@]+$'
    message = 'Enter a valid username. This value may contain only letters, numbers and ./_/@ characters.'
    flags = 0
