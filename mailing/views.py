from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from mailing.forms import ClientForm, Log_MailingForm, MailingForm
from mailing.models import Client, Log_Mailing, Mailing


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЯ ДЛЯ РАССЫЛОК'
    }


class ClientListView(ListView):
    model = Client
    form_class = ClientForm

    extra_context = {
        'title': 'СПИСОК ПОЛЬЗОВАТЕЛЕЙ ДЛЯ РАССЫЛОК'
    }


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПОЛЬЗОВАТЕЛЕЙ ДЛЯ РАССЫЛОК'
    }


class ClientDeleteView(DeleteView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ'
    }


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'СОЗДАНИЕ ПЕРИОДИЧНОСТИ ДЛЯ РАССЫЛКИ'
    }


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    form_class = MailingForm

    extra_context = {
        'title': 'ПРОСМОТР СПИСКА ПЕРИОДИЧНОСТИ РАССЫЛОК'
    }


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'УДАЛЕНИЕ РАССЫЛКИ'
    }


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПЕРИОДИЧНОСТИ РАССЫЛКИ'
    }


class Log_MailingListView(LoginRequiredMixin, ListView):
    model = Log_Mailing
    form_class = Log_MailingForm

    extra_context = {
        'title': 'ПРОСМОТР ЛОГОВ'
    }
