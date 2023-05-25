from .models import Account
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import AccountSerializer
from .permissions import IsAccountOwner
from rest_framework import generics


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
