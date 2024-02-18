from django.contrib import admin

from mailing.models import Client, Mailing, Log_Mailing, Text_Mailing


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'client_fio', 'client_comment',)
    list_filter = ('client_email', 'client_fio',)
    search_fields = ('client_email', 'client_fio',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('time_mailing', 'frequency',)
    list_filter = ('time_mailing', 'frequency',)
    search_fields = ('time_mailing', 'frequency',)


@admin.register(Text_Mailing)
class Text_MailingAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body',)
    list_filter = ('subject', 'body',)
    search_fields = ('subject', 'body',)


@admin.register(Log_Mailing)
class Log_MailingAdmin(admin.ModelAdmin):
    list_display = ('datatime_last_attempt', 'status_attempt', 'mailing',)
    list_filter = ('datatime_last_attempt', 'status_attempt', 'mailing',)
    search_fields = ('datatime_last_attempt', 'status_attempt', 'mailing',)
