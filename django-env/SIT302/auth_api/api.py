from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework import status, views
from rest_framework.response import Response

from .serializers import UserSerializer

class LoginView(views.APIView):

    @method_decorator(csrf_protect)
    def post(self, request):  # Sends the data to the server to process the request
        user = authenticate(username=request.data.get("username"),
                            password=request.data.get("password"))  # Compares the user and pass to what is in the server

        if user is None or not user.is_active:  # if this is incorrect this if statement runs
            return Response({
                'status': 'Unauthorized',
                'message': 'Username or password incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)  # If the code makes it here the user is logged in
        return Response(UserSerializer(user).data)  # the session is started here

class LogoutView(views.APIView):

    def get(self, request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
