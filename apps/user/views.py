from django.db.models import F
from rest_framework.pagination import PageNumberPagination
from apps.forum.utils.list_api_view import MyListAPIView
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status
from rest_framework.response import Response
from .models import Inivitation, User
from .serializers import UserSerializer, InivitationSerializer
import random

class PaginationReport(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class InivitationApiView(APIView):
    serializer_class = InivitationSerializer

    def get(self, request):
        invitations = Inivitation.objects.all()
        serializer = InivitationSerializer(instance=invitations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InivitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def generate_invitations(self, quantity):
        generated_invitations = []
        for _ in range(quantity):
            while True:
                random_code = random.randint(100000, 9999999)  
                if not Inivitation.objects.filter(code=random_code).exists():
                    break
            invitation = Inivitation(code=random_code)
            invitation.save()
            generated_invitations.append(invitation)
        return generated_invitations

    def post(self, request):
        quantity = request.data.get('quantity')
        if quantity is not None:
            generated_invitations = self.generate_invitations(quantity)
            serializer = InivitationSerializer(instance=generated_invitations, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'quantity': 'Quantity is required.'}, status=status.HTTP_400_BAD_REQUEST)


class InivitationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Inivitation.objects.all()
    serializer_class = InivitationSerializer


class UserApiView(MyListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PaginationReport


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
