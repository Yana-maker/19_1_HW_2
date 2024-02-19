from django import forms
from mailing.models import Client, Log_Mailing, Mailing, Text_Mailing


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('time_mailing', 'frequency', 'status_mailing',)


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_email', 'client_fio', 'client_comment',)


    def clean_client_email(self):
        cleaned_data = self.cleaned_data['client_email']
        if '@' not in cleaned_data:
            raise ValueError('почта должна содержать специальный символ "@')
        return cleaned_data




class Log_MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Log_Mailing
        fields = ('datatime_last_attempt', 'status_attempt', 'answer_mail_server', 'mailing', 'client',)



class Text_MailingForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Text_Mailing
        fields = ('subject', 'body', 'client_email', 'frequency',)
