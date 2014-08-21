from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, \
    DeleteView, DetailView

from .mixins import AppViewMixin, AppUserObjectsMixin, AppUserObjectMixin, \
    AppFormMixin, AppDeleteMixin


class AppList(AppViewMixin, AppUserObjectsMixin, ListView):
    template_name = 'mcoauth/apps/list.html'


class AppCreate(AppViewMixin, AppUserObjectMixin, AppFormMixin, CreateView):
    template_name = 'mcoauth/apps/create.html'
    form_valid_message = _('Application created')

    def get_initial(self):
        initial = super(AppCreate, self).get_initial()
        initial['url'] = 'http://'
        initial['redirect_uri'] = 'http://'
        return initial


class AppUpdate(AppViewMixin, AppUserObjectsMixin, AppFormMixin, UpdateView):
    template_name = 'mcoauth/apps/update.html'
    form_valid_message = _('Application updated')


class AppDelete(AppViewMixin, AppUserObjectsMixin, AppDeleteMixin, DeleteView):
    template_name = 'mcoauth/apps/delete.html'
    form_valid_message = _('Application deleted')


class AppCredentials(AppViewMixin, AppUserObjectsMixin, DetailView):
    template_name = 'mcoauth/apps/credentials.html'
