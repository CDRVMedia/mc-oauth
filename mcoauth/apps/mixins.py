from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from provider.oauth2.models import Client
from provider.oauth2.forms import ClientForm


class AppUserObjectMixin(object):
    model = Client


class AppEditObjectMixin(object):
    success_url = reverse_lazy('app:list')


class AppUserObjectsMixin(AppUserObjectMixin):
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class AppFormMixin(AppEditObjectMixin):
    form_class = ClientForm

    def form_valid(self, form):
        form.save(self.request.user)
        self.object = form.instance
        return redirect(self.get_success_url())
