from django.shortcuts import render
from django.views.generic import CreateView

from .forms import EmailInfromForm


def index(request):
    return render(request, 'inform/index.html')

class InformCreateView(CreateView):
    template_name = 'inform/send-email/index.html'
    form_class = EmailInfromForm
    success_url = '/send-inform-email'

    def form_valid(self, form):
        form.send_email()
        return super(InformCreateView, self).form_valid(form)

    def get_initial(self):
        initial = super(InformCreateView, self).get_initial()
        initial['company_name'] = 'اطلاعات مدیریت'
        return initial
