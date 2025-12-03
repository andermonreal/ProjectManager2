from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .authManager import UserManager
from .authService import LoginService, RegisterService
from .authSerializers import RegisterSerializer, LoginSerializer, UserSerializer, CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        registerService = RegisterService(UserManager())

        try:
            user = registerService.execute(email=data["email"], name=data["name"], password=data["password"], phone=data["phone"], birthday=data["birthday"])
            
            refresh = RefreshToken.for_user(user)
            print("llego aqui")
            print(refresh)
            print("llego aqui 2")
            print(user)
            print("llego aqui 3")
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'detail': "Valida el usuario con el correo"}, status=status.HTTP_200_OK)

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer


class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Sesión cerrada"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "Token inválido"}, status=status.HTTP_400_BAD_REQUEST)
