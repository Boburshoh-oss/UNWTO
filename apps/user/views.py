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
from django.shortcuts import get_object_or_404


class PaginationReport(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class InivitationApiView(APIView):
    serializer_class = InivitationSerializer
    pagination_class = PaginationReport

    def get(self, request):
        paginator = self.pagination_class()
        invitations = Inivitation.objects.all()
        result_page = paginator.paginate_queryset(invitations, request)
        serializer = InivitationSerializer(instance=result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
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
        quantity = request.data.get("quantity")
        if quantity is not None:
            generated_invitations = self.generate_invitations(quantity)
            serializer = InivitationSerializer(
                instance=generated_invitations, many=True
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"quantity": "Quantity is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class InvitationCheckApiView(APIView):
    serializer_class = InivitationSerializer
    pagination_class = PaginationReport

    def get(self, request):
        paginator = self.pagination_class()
        invitations = Inivitation.objects.all()
        result_page = paginator.paginate_queryset(invitations, request)
        serializer = InivitationSerializer(instance=result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        inputted_code = request.data.get('code')
        if inputted_code is not None:
            invitation = get_object_or_404(Inivitation, code=inputted_code)
            if invitation.active:
                serializer = InivitationSerializer(instance=invitation)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'code': 'Code already used.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'code': 'Code is required.'}, status=status.HTTP_400_BAD_REQUEST)



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
