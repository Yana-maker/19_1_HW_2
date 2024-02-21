import datetime

from django.db import models
from config import settings

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Frequency:
    choices = (
        ("ежедневно", "ежедневно"),
        ("еженедельно", "еженедельно"),
        ("ежемесячно", "ежемесячно"),
    )


class STATUS:
    choices = (
        ("создана", "создана"),
        ("запущена", "запущена"),
        ("завершена", "завершена"),
    )


class STATUS_ATTEMPT:
    choices = (
        ("успешно", "успешно"),
        ("не успешно", "не успешно"),
    )


class Client(models.Model):
    """ Клиент сервиса """
    client_email = models.EmailField(unique=True, verbose_name='почта')
    client_fio = models.CharField(max_length=500, verbose_name='фио')
    client_comment = models.CharField(max_length=500, verbose_name='комментарий')
    owner_client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                     verbose_name='автор:')

    def __str__(self):
        return f"{self.client_fio}"

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('client_fio',)


class Text_Mailing(models.Model):
    """ Сообщение для рассылки """
    subject = models.CharField(verbose_name='тема письма', **NULLABLE)
    body = models.CharField(verbose_name='тело письма', **NULLABLE)
    owner_text_mailing = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                           verbose_name='автор:')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('subject',)


class Mailing(models.Model):
    """ Рассылка (настройки) """
    time_mailing = models.DateTimeField(default=datetime.datetime.now(), verbose_name='время рассылки')
    frequency = models.CharField(max_length=20, choices=Frequency.choices, default='ежедневно',
                                 verbose_name='периодичность')
    status_mailing = models.CharField(max_length=20, default='создана', choices=STATUS.choices, verbose_name='статус')
    massage = models.ForeignKey(Text_Mailing, on_delete=models.SET_NULL, **NULLABLE,
                                verbose_name='сообщение:')

    client_email = models.ManyToManyField(Client, verbose_name='клиенты')
    owner_mailing = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                      verbose_name='автор:')

    def __str__(self):
        return f'{self.frequency}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('frequency',)


class Log_Mailing(models.Model):
    datatime_last_attempt = models.DateTimeField(verbose_name='дата и время последней попытки')
    status_attempt = models.CharField(choices=STATUS_ATTEMPT.choices, verbose_name='статус попытки')
    answer_mail_server = models.TextField(**NULLABLE, verbose_name='ответ почтового сервера')
    mailing = models.ForeignKey(Mailing, verbose_name='рассылка', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.status_attempt}"

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылки'
        ordering = ('status_attempt',)
