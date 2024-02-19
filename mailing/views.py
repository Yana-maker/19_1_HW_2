from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from mailing.forms import ClientForm, Log_MailingForm, MailingForm, Text_MailingForm
from mailing.models import Client, Log_Mailing, Mailing, Text_Mailing


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:Clientlist')
    permission_required = 'mailing.add_client'

    extra_context = {
        'title': 'ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ ДЛЯ РАССЫЛОК'
    }


class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    form_class = ClientForm
    permission_required = 'mailing.view_client'

    extra_context = {
        'title': 'СПИСОК ПОЛЬЗОВАТЕЛЕЙ ДЛЯ РАССЫЛОК'
    }


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:Clientlist')
    permission_required = 'mailing.change_client'

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПОЛЬЗОВАТЕЛЕЙ ДЛЯ РАССЫЛОК'
    }


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Client
    form_class = ClientForm
    permission_required = 'mailing.view_client'

    extra_context = {
        'title': 'ПРОСМОТР ПОЛЬЗОВАТЕЛЯ'
    }


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:Clientlist')
    permission_required = 'mailing.delete_client'

    extra_context = {
        'title': 'УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ'
    }


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')
    permission_required = 'mailing.add_mailing'

    extra_context = {
        'title': 'СОЗДАНИЕ ПЕРИОДИЧНОСТИ ДЛЯ РАССЫЛКИ'
    }


class MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailing.view_mailing'

    extra_context = {
        'title': 'ПРОСМОТР СПИСКА ПЕРИОДИЧНОСТИ РАССЫЛОК'
    }


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailing.view_mailing'

    extra_context = {
        'title': 'ПРОСМОТР рассылки'
    }




class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')
    permission_required = 'mailing.delete_mailing'

    extra_context = {
        'title': 'УДАЛЕНИЕ РАССЫЛКИ'
    }


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')
    permission_required = 'mailing.change_mailing'

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПЕРИОДИЧНОСТИ РАССЫЛКИ'
    }


class Log_MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Log_Mailing
    form_class = Log_MailingForm
    permission_required = 'mailing.view_log_mailing'

    extra_context = {
        'title': 'ПРОСМОТР ЛОГОВ'
    }



class Text_MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Text_Mailing
    form_class = Text_MailingForm
    success_url = reverse_lazy('mailing:list')
    permission_required = 'mailing.add_text_mailing'

    extra_context = {
        'title': 'СОЗДАНИЕ ПЕРИОДИЧНОСТИ ДЛЯ РАССЫЛКИ'
    }


class Text_MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Text_Mailing
    form_class = Text_MailingForm
    permission_required = 'mailing.view_text_mailing'

    extra_context = {
        'title': 'ПРОСМОТР СПИСКА ПЕРИОДИЧНОСТИ РАССЫЛОК'
    }


class Text_MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Text_Mailing
    form_class = Text_MailingForm
    success_url = reverse_lazy('mailing:list')
    permission_required = 'mailing.delete_text_mailing'

    extra_context = {
        'title': 'УДАЛЕНИЕ РАССЫЛКИ'
    }


class Text_MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Text_Mailing
    form_class = Text_MailingForm
    permission_required = 'mailing.change_text_mailing'
    success_url = reverse_lazy('mailing:Text_Mailinglist')

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ТЕКСТА РАССЫЛКИ'
    }


class Text_MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Text_Mailing
    form_class = Text_MailingForm
    permission_required = 'mailing.view_text_mailing'

    extra_context = {
        'title': 'ПРОСМОТР ТЕКСТА РАССЫЛКИ'
    }