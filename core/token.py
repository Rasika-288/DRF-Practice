import jwt

from django.conf import settings

def get_jwt_token(user):
    encoded = jwt.encode({'user_id':user.id}, settings.SECRET_KEY, algorithm='HS256')
    return encoded

def decode_jwt_token(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')