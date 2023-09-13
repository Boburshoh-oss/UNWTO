from .models import Inivitation
from django.db import IntegrityError
from django.forms import ValidationError
import random
from config.settings.base import get_env_value
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

OWN_EMAIL = get_env_value("OWN_EMAIL")  # Receivers gmail address
# Google App password NOT gmail password
OWN_PASSWORD = get_env_value("OWN_PASSWORD")


def get_uid():
    code = "".join(random.choices("0123456789asdfghjklqwertyuiopzxcvbnm!@$%&?_-", k=7))
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


def send_email(first_name, last_name, email, access_id, lang):
    msg = MIMEMultipart()
    msg["From"] = "unwtoforum2023@gmail.com"
    msg["To"] = email

    if lang == "ru":
        msg["Subject"] = "Пригласительная"
        text = f"Уважаемый {first_name} {last_name}!\nВаш ID код: \n{access_id}"
        email_message = MIMEText(text, "plain", "utf-8")
    elif lang == "uz":
        msg["Subject"] = "Taklifnoma"
        email_message = MIMEText(
            f"Hurmatli {first_name} {last_name}!\nSizning ID raqamingiz: \n{access_id}",
            "plain",
        )
    else:
        msg["Subject"] = "Invitation"
        email_message = MIMEText(
            f"Dear {first_name} {last_name}!\nYour ID: \n{access_id}", "plain"
        )

    msg.attach(email_message)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(
            "unwtoforum2023@gmail.com", "lzlpfadqzlpwmqpt"
        )  # Better to store this in environment variables
        connection.sendmail(
            from_addr="unwtoforum2023@gmail.com", to_addrs=email, msg=msg.as_string()
        )
