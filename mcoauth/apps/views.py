from django.views.generic import ListView, CreateView, UpdateView, \
    DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from provider.oauth2.models import Client
from provider.oauth2.forms import ClientForm


class AppList(ListView):
    template_name = 'mcoauth/apps/list.html'

    def get_queryset(self):
        return Client.objects.filter(user=self.request.user)


class AppCreate(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mcoauth/apps/create.html'
    success_url = reverse_lazy('app:list')

    def form_valid(self, form):
        form.save(self.request.user)
        self.object = form.instance
        return redirect(self.get_success_url())


class AppUpdate(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mcoauth/apps/update.html'
    success_url = reverse_lazy('app:list')


class AppDelete(DeleteView):
    model = Client
    template_name = 'mcoauth/apps/delete.html'
    success_url = reverse_lazy('app:list')


class AppCredentials(DetailView):
    model = Client
    template_name = 'mcoauth/apps/credentials.html'
