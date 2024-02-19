from django.contrib import admin

from mailing.models import Client, Mailing, Log_Mailing, Text_Mailing


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client_email', 'client_fio', 'client_comment',)
    list_filter = ('client_email', 'client_fio',)
    search_fields = ('pk', 'client_email', 'client_fio',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time_mailing', 'frequency',)
    list_filter = ('time_mailing', 'frequency',)
    search_fields = ('pk', 'time_mailing', 'frequency',)


@admin.register(Text_Mailing)
class Text_MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'body',)
    list_filter = ('subject', 'body',)
    search_fields = ('pk', 'subject', 'body',)


@admin.register(Log_Mailing)
class Log_MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'datatime_last_attempt', 'status_attempt', 'mailing',)
    list_filter = ('datatime_last_attempt', 'status_attempt', 'mailing',)
    search_fields = ('pk', 'datatime_last_attempt', 'status_attempt', 'mailing',)
