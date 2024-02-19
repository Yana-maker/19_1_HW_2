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

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_client=self.request.user
        )


class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    form_class = ClientForm
    permission_required = 'mailing.view_client'

    extra_context = {
        'title': 'СПИСОК ПОЛЬЗОВАТЕЛЕЙ ДЛЯ РАССЫЛОК'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_client=self.request.user
        )


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:Clientlist')
    permission_required = 'mailing.change_client'

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПОЛЬЗОВАТЕЛЕЙ ДЛЯ РАССЫЛОК'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_client=self.request.user
        )


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Client
    form_class = ClientForm
    permission_required = 'mailing.view_client'

    extra_context = {
        'title': 'ПРОСМОТР ПОЛЬЗОВАТЕЛЯ'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_client=self.request.user
        )


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:Clientlist')
    permission_required = 'mailing.delete_client'

    extra_context = {
        'title': 'УДАЛЕНИЕ ПОЛЬЗОВАТЕЛЯ'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_client=self.request.user
        )


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')
    permission_required = 'mailing.add_mailing'

    extra_context = {
        'title': 'СОЗДАНИЕ ПЕРИОДИЧНОСТИ ДЛЯ РАССЫЛКИ'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_mailing=self.request.user
        )


class MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailing.view_mailing'

    extra_context = {
        'title': 'ПРОСМОТР СПИСКА ПЕРИОДИЧНОСТИ РАССЫЛОК'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_mailing=self.request.user
        )


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailing.view_mailing'

    extra_context = {
        'title': 'ПРОСМОТР рассылки'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_mailing=self.request.user
        )




class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')
    permission_required = 'mailing.delete_mailing'

    extra_context = {
        'title': 'УДАЛЕНИЕ РАССЫЛКИ'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_mailing=self.request.user
        )


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')
    permission_required = 'mailing.change_mailing'

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ПЕРИОДИЧНОСТИ РАССЫЛКИ'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_mailing=self.request.user
        )


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

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_text_mailing=self.request.user
        )


class Text_MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Text_Mailing
    form_class = Text_MailingForm
    permission_required = 'mailing.view_text_mailing'

    extra_context = {
        'title': 'ПРОСМОТР СПИСКА ПЕРИОДИЧНОСТИ РАССЫЛОК'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_text_mailing=self.request.user
        )


class Text_MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Text_Mailing
    form_class = Text_MailingForm
    success_url = reverse_lazy('mailing:list')
    permission_required = 'mailing.delete_text_mailing'

    extra_context = {
        'title': 'УДАЛЕНИЕ РАССЫЛКИ'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_text_mailing=self.request.user
        )


class Text_MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Text_Mailing
    form_class = Text_MailingForm
    permission_required = 'mailing.change_text_mailing'
    success_url = reverse_lazy('mailing:Text_Mailinglist')

    extra_context = {
        'title': 'РЕДАКТИРОВАНИЕ ТЕКСТА РАССЫЛКИ'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_text_mailing=self.request.user
        )


class Text_MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Text_Mailing
    form_class = Text_MailingForm
    permission_required = 'mailing.view_text_mailing'

    extra_context = {
        'title': 'ПРОСМОТР ТЕКСТА РАССЫЛКИ'
    }

    def get_queryset(self):
        return super().get_queryset().filter(
            owner_text_mailing=self.request.user
        )