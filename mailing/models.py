import datetime

from django.db import models
from config import settings

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Client(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    client_email = models.EmailField(unique=True, verbose_name='почта')
    client_fio = models.CharField(max_length=500, verbose_name='фио')
    client_comment = models.CharField(max_length=500, verbose_name='комментарий')

    def __str__(self):
        return f"{self.client_fio}"

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('client_fio',)


class Frequency:
    choices = (
        ("ежедневно", "daily"),
        ("еженедельно", "weekly"),
        ("ежемесячно", "monthly"),
    )


class Mailing(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(unique=True, verbose_name='название')
    time = models.DateTimeField(default=datetime.datetime.now(), verbose_name='время и дата рассылки')
    frequency = models.CharField(max_length=11, choices=Frequency.choices, default='daily',
                                 verbose_name='периодичность')
    mailing_status = models.CharField(default='создана', choices=settings.STATUS, **NULLABLE, verbose_name='статус')
    client_email = models.ManyToManyField('Client', verbose_name='клиенты')
    subject = models.CharField(verbose_name='тема письма', **NULLABLE)
    body = models.CharField(verbose_name='тело письма', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('frequency',)



class Log_Mailing(models.Model):
    datatime_last_attempt = models.DateTimeField(verbose_name='дата и время последней попытки')
    status_attempt = models.CharField(choices=settings.STATUS_ATTEMPT, verbose_name='статус попытки')
    answer_mail_server = models.TextField(**NULLABLE, verbose_name='ответ почтового сервера')
    mailing = models.ForeignKey(Mailing, verbose_name='название', on_delete=models.CASCADE, **NULLABLE)
    client = models.ForeignKey(Client, verbose_name='клиентs', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.status_attempt}"

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылки'
        ordering = ('status_attempt',)
