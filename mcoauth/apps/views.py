from django.views.generic import ListView, CreateView, UpdateView, \
    DeleteView, DetailView

from .mixins import AppUserObjectsMixin, AppUserObjectMixin, AppFormMixin, \
    AppEditObjectMixin


class AppList(AppUserObjectsMixin, ListView):
    template_name = 'mcoauth/apps/list.html'


class AppCreate(AppUserObjectMixin, AppFormMixin, CreateView):
    template_name = 'mcoauth/apps/create.html'

    def get_initial(self):
        initial = super(AppCreate, self).get_initial()
        initial['url'] = 'http://'
        initial['redirect_uri'] = 'http://'
        return initial


class AppUpdate(AppUserObjectsMixin, AppFormMixin, UpdateView):
    template_name = 'mcoauth/apps/update.html'


class AppDelete(AppUserObjectsMixin, AppEditObjectMixin, DeleteView):
    template_name = 'mcoauth/apps/delete.html'


class AppCredentials(AppUserObjectsMixin, DetailView):
    template_name = 'mcoauth/apps/credentials.html'
