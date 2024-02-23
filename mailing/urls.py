from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingUpdateView, MailingListView, ClientCreateView, ClientListView, \
    ClientUpdateView, MailingDeleteView, \
    ClientDeleteView, Text_MailingCreateView, Text_MailingDeleteView, Text_MailingUpdateView, Text_MailingListView, \
    Log_MailingListView, MailingDetailView, ClientDetailView, Text_MailingDetailView, Log_mailingDetailView, \
    Log_mailingDeleteView

app_name = MailingConfig.name

urlpatterns = [

    path('create/', MailingCreateView.as_view(), name='create'),
    path('list/', cache_page(10)(MailingListView.as_view()), name='list'),
    path('view/<int:pk>/', cache_page(10)(MailingDetailView.as_view()), name='view'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),
    path('Client/create/', ClientCreateView.as_view(), name='Clientсreate'),
    path('Client/view/<int:pk>/', cache_page(10)(ClientDetailView.as_view()), name='Clientview'),
    path('Client/list/', cache_page(10)(ClientListView.as_view()), name='Clientlist'),
    path('Client/edit/<int:pk>/', ClientUpdateView.as_view(), name='Clientedit'),
    path('Client/delete/<int:pk>/', ClientDeleteView.as_view(), name='Clientdelete'),
    path('Text_Mailing/create/', Text_MailingCreateView.as_view(), name='Text_Mailingcreate'),
    path('Text_Mailing/list/', cache_page(10)(Text_MailingListView.as_view()), name='Text_Mailinglist'),
    path('Text_Mailing/edit/<int:pk>/', Text_MailingUpdateView.as_view(), name='Text_Mailingedit'),
    path('Text_Mailing/delete/<int:pk>/', Text_MailingDeleteView.as_view(), name='Text_Mailingdelete'),
    path('Text_Mailingview/view/<int:pk>/', cache_page(10)(Text_MailingDetailView.as_view()), name='Text_Mailingview'),
    path('Log_Mailing/list/', cache_page(10)(Log_MailingListView.as_view()), name='Log_Mailinglist'),
    path('Log_Mailing/view/<int:pk>/', cache_page(10)(Log_mailingDetailView.as_view()), name='Log_Mailingview'),
    path('Log_Mailing/delete/<int:pk>/', cache_page(10)(Log_mailingDeleteView.as_view()), name='Log_Mailingdelete'),
]
