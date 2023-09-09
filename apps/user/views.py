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


class PaginationReport(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class InivitationApiView(APIView):
    serializer_class = InivitationSerializer
    pagination_class = PaginationReport

    def get(self, request):
        invitation = Inivitation.objects.all()
        serializer = InivitationSerializer(instance=invitation, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InivitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            inputted_code = request.data.get('code')  # Get the inputted code
            return Response({'code': inputted_code}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
