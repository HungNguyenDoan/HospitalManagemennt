import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
from .models import Staff
class SafeJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return None

        try:
            token_prefix, access_token = authorization_header.split(' ')
            if token_prefix != 'Bearer':
                raise exceptions.AuthenticationFailed('Invalid token prefix')
            
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Access token expired')
        except ValueError:
            raise exceptions.AuthenticationFailed('Invalid token format')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')
        
        staff_id = payload.get('staff_id')
        if staff_id is None:
            raise exceptions.AuthenticationFailed('Staff ID not found in token payload')
        
        staff = Staff.objects.filter(id=staff_id).first()
        if staff is None:
            raise exceptions.AuthenticationFailed('Staff not found')

        if not staff.is_active:
            raise exceptions.AuthenticationFailed('Staff is inactive')

        return (staff, None)
