import datetime
import jwt
from django.conf import settings


def generate_access_token(staff_id):
    access_token_payload = {
        'staff_id': staff_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
        settings.SECRET_KEY, algorithm='HS256')
    return access_token


def generate_refresh_token(staff_id):
    refresh_token_payload = {
        'staff_id': staff_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm='HS256')
    return refresh_token