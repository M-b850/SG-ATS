from email.mime import text
from django import forms
from django.forms import widgets
from core.models import Person
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings

from utils.email import enter_data_to_html

class EmailInfromForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'input--style-4'}),
            'password': widgets.PasswordInput(attrs={'class': 'input--style-4', 'type': 'text'}),
            'email': widgets.EmailInput(attrs={'class': 'input--style-4'}),
            'supervisor_name': widgets.TextInput(attrs={'class': 'input--style-4'}),
            'system_number': widgets.TextInput(attrs={'class': 'input--style-4'}),
            'company_name': widgets.TextInput(attrs={'class': 'input--style-4'}),
        }
    def send_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        supervisor_name = self.cleaned_data.get('supervisor_name')
        system_number = self.cleaned_data.get('system_number')
        company_name = self.cleaned_data.get('company_name')

        # send html to email
        # supervisor_name, system_number, company_name, password
        data = {
            'username': username,
            'password': password,
            'supervisor_name': supervisor_name,
            'system_number': system_number,
            'company_name': company_name,
        }
        html_content = enter_data_to_html(data)
        text_content = 'This is an important message.'
        from_email = settings.EMAIL_HOST_USER
        to = email
        subject = 'همکاران سیستم'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()