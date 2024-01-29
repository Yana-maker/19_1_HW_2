from django.contrib import admin

from mailing.models import Client, Mailing, Log_Mailing


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'client_fio', 'client_comment',)
    list_filter = ('client_email', 'client_fio',)
    search_fields = ('client_email', 'client_fio',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'frequency',)
    list_filter = ('name', 'frequency',)
    search_fields = ('name', 'frequency',)


@admin.register(Log_Mailing)
class Log_MailingAdmin(admin.ModelAdmin):
    list_display = ('datatime_last_attempt', 'status_attempt', 'mailing',)
    list_filter = ('datatime_last_attempt', 'status_attempt', 'mailing',)
    search_fields = ('datatime_last_attempt', 'status_attempt', 'mailing',)
