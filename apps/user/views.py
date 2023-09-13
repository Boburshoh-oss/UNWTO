from rest_framework.pagination import PageNumberPagination
from apps.forum.utils.list_api_view import MyListAPIView
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from rest_framework import status
from rest_framework.response import Response
from .models import Inivitation, User
from .serializers import UserSerializer, InivitationSerializer
from django.shortcuts import get_object_or_404
from .utils import create_invitaion
from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse, HttpResponseNotFound
import os
from rest_framework.renderers import MultiPartRenderer
from rest_framework.decorators import renderer_classes, api_view
class PaginationReport(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class InivitationApiView(APIView):
    serializer_class = InivitationSerializer
    pagination_class = PaginationReport

    def get(self, request):
        paginator = self.pagination_class()
        invitations = Inivitation.objects.all().order_by("-pk")
        result_page = paginator.paginate_queryset(invitations, request)
        serializer = InivitationSerializer(instance=result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        try:
            num_of_invs = int(request.data["quantity"])
        except (KeyError, TypeError, ValueError):
            return Response({"error": "Invalid input"})

        if num_of_invs <= 0 or num_of_invs > 10000:
            return Response(
                {"error": "Number of invitations must be between 1 and 10,000"}
            )

        invitations = create_invitaion(num_of_invs)

        if invitations:
            serializer = InivitationSerializer(invitations, many=True)
            return Response(
                {
                    "success": f"{num_of_invs} invitations created",
                    "codes": serializer.data,
                }
            )
        else:
            return Response({"error": "Invitations creation failed"})


class InvitationCheckApiView(APIView):
    serializer_class = InivitationSerializer
    pagination_class = PaginationReport

    def get(self, request):
        paginator = self.pagination_class()
        invitations = Inivitation.objects.all().order_by("-pk")
        result_page = paginator.paginate_queryset(invitations, request)
        serializer = InivitationSerializer(instance=result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        inputted_code = request.data.get("code")
        if inputted_code is not None:
            invitation = get_object_or_404(Inivitation, code=str(inputted_code))
            if invitation.active:
                serializer = InivitationSerializer(instance=invitation)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"code": "Code already used."}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {"code": "Code is required."}, status=status.HTTP_400_BAD_REQUEST
        )


class InivitationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Inivitation.objects.all()
    serializer_class = InivitationSerializer


class UserApiView(MyListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def search(request):
    try:
        number = int(request.POST.get("code"))
    except (KeyError, TypeError, ValueError):
        return Response({"error": "Invalid input"})

    if number <= 0 or number > 10000:
        return Response({"error": "Number of invitations must be between 1 and 10,000"})

    invitations = create_invitaion(number)
    with open("media/invitaions.txt", "a") as file:
        for inv in invitations:
            file.write(inv.code + "\n")
    content = {
        'message' : f"{number} invitations created successfully!",
        "yaratildi": "true"
    }
    return render(request, "entities/index.html", context=content)


def download_invitations(request):
   return redirect('/media/invitaions.txt')
