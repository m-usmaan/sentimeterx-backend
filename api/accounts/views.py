from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.exceptions import ValidationError
from api.organizations.models import Organization


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        organization_slug = request.data.get('organization_slug')
        if not organization_slug:
            raise ValidationError({'organization_slug': 'This field is required.'})

        try:
            organization = Organization.objects.get(slug=organization_slug, is_active=True)
        except Organization.DoesNotExist:
            raise ValidationError({'authorization': 'Organization does not exist.'})

        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        if user.organization != organization:
            raise ValidationError({'authorization': 'Unable to log in with provided credentials.'})

        login(request, user)
        return super().post(request, format=None)
