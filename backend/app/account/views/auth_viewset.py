"""
Module containing the API Auth views.
"""

from django.contrib.auth import login, logout

from rest_framework import permissions, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from account.models import User
from account.serializers import UserSerializer


class AuthViewSet(viewsets.ViewSet):
    """
    API endpoints to handle user authentication.
    """
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=["post"], url_path="register", url_name="register")
    def register(self, request: Request) -> Response:
        """
        API Endpoint to register a new user by:
            1. Creating the user;
            2. Creating a new token for this user;
            3. Returning the user data and the token.
        """
        body: dict[str, str] = request.data # type: ignore

        try:
            name = body["name"]
            email = body["email"]
            password = body["password"]

        except KeyError:
            response = {"error": "Missing required fields."}
            return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        user, created = User.objects.get_or_create(
            email=email,
            username=email,
            name=name,
        )

        if not created:
            response = {"error": "User already exists."}
            return Response(response, status=status.HTTP_409_CONFLICT)
        
        user.set_password(password)
        user.save()

        token, _ = Token.objects.get_or_create(user=user)

        login(request, user)

        user_serializer = UserSerializer(user)

        response = {
            "user": user_serializer.data,
            "token": token.key,
        }
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="login", url_name="login")
    def login(self, request: Request, *args, **kwargs) -> Response:
        """
        API Endpoint to login a user by:
            1. Validating the user credentials;
            2. Logging the user in;
        """
        body: dict[str, str] = request.data # type: ignore

        try:
            email = body["email"]
            password = body["password"]

        except KeyError:
            response = {"error": "Missing required fields."}
            return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if email is None or password is None:
            response = {'error': 'Please provide both email and password'}
            return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        user = User.objects.filter(email=email).first()
        if user is None:
            response = {'error': 'Invalid email'}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            response = {'error': 'Invalid password'}
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)

        login(request, user)

        user_serializer = UserSerializer(user)

        response = {
            'user': user_serializer.data, 
            'token': token.key
        }
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="logout", url_name="logout")
    def logout(self, request: Request, *args, **kwargs) -> Response:
        """
        API Endpoint to logout a user by:
            1. Logging the user out;
        """
        request.user.auth_token.delete()
        logout(request)

        response = {'message': 'User logged out successfully'}
        return Response(response)

