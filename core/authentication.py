from django.contrib.auth.models import User
# from .models import User

from rest_framework import authentication
from rest_framework import exceptions

from core.token import decode_jwt_token

# from web_development.User.models import User


class JwtAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if not token:
            return None

        payload = decode_jwt_token(token)

        try:
            user = User.objects.get(id=payload['user_id'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return user, None