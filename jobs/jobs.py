from config import settings
from config.settings import TIME_ZONE
import datetime
import pytz
from django.core.mail import send_mail
from mailing.models import Mailing, Log_Mailing, Client, Text_Mailing





def send_mailings():

    mailing = Text_Mailing.objects.get()
    client = Client.objects.get()


    try:
        send_mail(
            subject=mailing.subject,
            message=mailing.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.client_email],
        )
        Log_Mailing.objects.create(
            mailing=mailing.subject,
            datatime_last_attempt=datetime.datetime.now(),
            status_attempt='УСПЕШНО',
        )

    except Exception as e:
        Log_Mailing.objects.create(
            datatime_last_attempt=datetime.datetime.now(),
            status_attempt='НЕ УСПЕШНО',
            answer_mail_server=e
        )




