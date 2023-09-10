from .models import Inivitation
from os import geteuid
from django.db import IntegrityError
from django.forms import ValidationError
import random


def get_uid():
    code ="".join(random.choices("0123456789", k=7))
    inv = Inivitation.objects.filter(code=code).exists()
    if inv:
        get_uid()
    return code


def create_invitaion(num_of_qrcodes):
    codes = [Inivitation() for _ in range(num_of_qrcodes)]

    # set the created_at field to the current time for all objects
    for qr in codes:
        qr.code = geteuid()
    try:
        # use bulk_create to create all the objects in a single query
        inv_codes = Inivitation.objects.bulk_create(codes)
        return inv_codes
    except (IntegrityError, ValidationError):
        return []
