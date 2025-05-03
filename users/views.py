from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from .models import Dealer
from .serializers import RegisterSerializer, UserSerializer, DealerSerializer
from .pagination import DealerPagination


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=400)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out."}, status=200)
        except TokenError:
            return Response({"error": "Invalid token"}, status=400)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    pagination_class = DealerPagination
    permission_classes = [IsAuthenticated]