from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
from users.models import User
import jwt
from django.conf import settings

class JWTAuthetication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(" ")

        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed(" Invalid Token")
        
        token = auth_token[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")

            username = payload['username']
            user = User.objects.get(username=username)

            return (user, token)

        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed('Token has expired or ' + str(ex) + ' login again')
        
        except jwt.DecodeError as decode_error:
            raise exceptions.AuthenticationFailed('Invalid token login again')
        
        except User.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed('User Does not exist')

        return super().authenticate(request)