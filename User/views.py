from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
from django.utils import timezone
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from core.token import get_jwt_token
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer



class SignUpApi(APIView):
    # permission_classes = (AllowAny)
    def post(self, request):
        request.data['created_at'] = timezone.now()
        request.data['password'] = make_password(request.data['password'])
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_jwt_token(user)
            return Response(
                data={
                    'message': "User Created Successfully",
                    'token': token,
                    'code': "100"
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={
                    'messages': serializer.errors,
                    'code': "200"
                },
                status=status.HTTP_200_OK
            )

class UserApi(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        # token = request.META['HTTP_AUTHORIZATION']
        # payload = decode_jwt_token(token)
        # user = User.objects.get(id=payload['user_id'])

        serializer = UserSerializer(request.user)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )



class LoginApi(APIView):
    permission_classes = (AllowAny)
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.get(email=email)
        if check_password(password, user.password):
            token = get_jwt_token(user)
            return Response(
                data={
                    'message':'Login Successfull',
                    'token' :token,
                    'code':'200'

                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={
                    'message':'Email or Password is Wrong',
                    'code':'200'
                },
                status=status.HTTP_200_OK
            )
