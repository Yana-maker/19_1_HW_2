from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingUpdateView, MailingListView, ClientCreateView, ClientListView, \
    ClientUpdateView, MailingDeleteView, \
    ClientDeleteView

app_name = MailingConfig.name

urlpatterns = [

    path('create/', MailingCreateView.as_view(), name='create'),
    path('list/', MailingListView.as_view(), name='list'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='delete'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('list/', ClientListView.as_view(), name='list'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete'),
]
