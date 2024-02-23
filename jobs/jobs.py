import datetime
import logging


from config import settings


from mailing.models import Mailing, Log_Mailing, STATUS_ATTEMPT
from apscheduler.triggers.cron import CronTrigger
from django.core.mail import send_mail



def add_jobs_period(scheduler):
    mailing_one_day = Mailing.objects.filter(frequency='ежедневно')
    mailing_one_week = Mailing.objects.filter(frequency='еженедельно')
    mailing_one_month = Mailing.objects.filter(frequency='ежемесячно')

    if mailing_one_day:
        scheduler.add_job(
            send_mailings,
            trigger=CronTrigger(hour="*/24"),  # Every day
            id="send_mailings",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,

        )

    if mailing_one_week:
        scheduler.add_job(
            send_mailings,
            trigger=CronTrigger(day_of_week="*/1"),  # 1 раз в неделю
            id="send_mailings",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )

    if mailing_one_month:
        scheduler.add_job(
            send_mailings,
            trigger=CronTrigger(week="*/4"),  # 1 раз в месяц
            id="send_mailings",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )


def send_mailings():

    logging.info('начилась рассылка')
    mailings = Mailing.objects.filter(status_mailing="создана")
    for mailing in mailings:
        clients = mailing.client_email.all()
        sub = mailing.massage.subject
        body = mailing.massage.body
        client_email = [client.client_email for client in clients]

        try:
            send_mail(
                subject=sub,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=client_email,
            )

            log = Log_Mailing(
                mailing=mailing,
                datatime_last_attempt=datetime.datetime.now(),
                status_attempt='успешно'
            )
            log.save()

            
            mailing.status_mailing = "запущена"
            mailing.save()

        except Exception as e:
            logging.exception('поймали ошибку')
            log = Log_Mailing(
                mailing=mailing,
                datatime_last_attempt=datetime.datetime.now(),
                status_attempt='не успешно',
                answer_mail_server=e,
            )
            log.save()

        mailing.status_mailing = "завершена"
        mailing.save()

