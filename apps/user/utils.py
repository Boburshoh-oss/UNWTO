from .models import Inivitation
from django.db import IntegrityError
from django.forms import ValidationError
import random
from config.settings.base import get_env_value
import smtplib
# from validate_email_address import validate_email
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


def is_valid_email(email):
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            status, _ = connection.verify(email)
            return status == 250  # 250 indicates a valid email address
    except smtplib.SMTPException:
        return False

def send_email(first_name, last_name, email, access_id):
    if not is_valid_email(email):
        print(f"Invalid email address: {email}")
        return

    email_message = f"Subject:Taklifnoma\nHurmatli {first_name} {last_name}!\nSizning ID raqamingiz: {access_id}"

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(OWN_EMAIL, OWN_PASSWORD)
            con = connection.sendmail(from_addr=OWN_EMAIL, to_addrs=email, msg=email_message)
            print(con, '*'*20)
    except Exception as e:
        print(f"An error occurred: {e}")