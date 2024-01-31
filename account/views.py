from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated


class RegistrationView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            'Аккаунт успешно создан', status=201
        )


class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response(
                'Аккаунт успешно активирован',
                status=200
            )


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer  

      
# class SomeView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response('helloooooooo')