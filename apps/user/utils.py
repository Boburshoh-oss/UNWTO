from .models import Inivitation
from django.db import IntegrityError
from django.forms import ValidationError
import random
from config.settings.base import get_env_value
import smtplib
OWN_EMAIL = get_env_value("OWN_EMAIL")  # Receivers gmail address
# Google App password NOT gmail password
OWN_PASSWORD = get_env_value("OWN_PASSWORD")

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
        qr.code = get_uid()
    try:
        # use bulk_create to create all the objects in a single query
        inv_codes = Inivitation.objects.bulk_create(codes)
        return inv_codes
    except (IntegrityError, ValidationError):
        return []


def send_email(first_name,last_name, email, access_id):
    """In order to use SMPTLIB, you have to give permission to receivers gmail, acception external mails. FOr this turn on TWO STEP VERIFICATION on accaunt settings and create new app. user given 16 char app`s password as host email`s password"""
    email_message = f"Subject:Taklifnoma\nHurmatli {first_name} {last_name}!\nSizning ID raqamingiz: \n{access_id}"
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        con = connection.sendmail(from_addr=OWN_EMAIL, to_addrs=email, msg=email_message)