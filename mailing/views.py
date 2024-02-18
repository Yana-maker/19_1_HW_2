from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from mailing.forms import ClientForm, Log_MailingForm, MailingForm, Text_MailingForm
from mailing.models import Client, Log_Mailing, Mailing, Text_Mailing


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:Clientlist')

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
    success_url = reverse_lazy('mailing:Clientlist')

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПОЛЬЗОВАТЕЛЕЙ ДЛЯ РАССЫЛОК'
    }


class ClientDetailView(DetailView):
    model = Client
    form_class = ClientForm

    extra_context = {
        'title': 'ПРОСМОТР ПОЛЬЗОВАТЕЛЯ'
    }


class ClientDeleteView(DeleteView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:Clientlist')

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


class MailingDetailView(DetailView):
    model = Mailing
    form_class = MailingForm

    extra_context = {
        'title': 'ПРОСМОТР рассылки'
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



class Text_MailingCreateView(LoginRequiredMixin, CreateView):
    model = Text_Mailing
    form_class = Text_MailingForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'СОЗДАНИЕ ПЕРИОДИЧНОСТИ ДЛЯ РАССЫЛКИ'
    }


class Text_MailingListView(LoginRequiredMixin, ListView):
    model = Text_Mailing
    form_class = Text_MailingForm

    extra_context = {
        'title': 'ПРОСМОТР СПИСКА ПЕРИОДИЧНОСТИ РАССЫЛОК'
    }


class Text_MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Text_Mailing
    form_class = Text_MailingForm
    success_url = reverse_lazy('mailing:list')

    extra_context = {
        'title': 'УДАЛЕНИЕ РАССЫЛКИ'
    }


class Text_MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Text_Mailing
    form_class = Text_MailingForm
    success_url = reverse_lazy('mailing:Text_Mailinglist')

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПЕРИОДИЧНОСТИ РАССЫЛКИ'
    }
