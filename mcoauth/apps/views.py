from django.views.generic import ListView, CreateView, UpdateView, \
    DeleteView, DetailView

from braces.views import LoginRequiredMixin

from .mixins import AppUserObjectsMixin, AppUserObjectMixin, AppFormMixin, \
    AppEditObjectMixin


class AppViewMixin(LoginRequiredMixin):
    pass


class AppList(AppViewMixin, AppUserObjectsMixin, ListView):
    template_name = 'mcoauth/apps/list.html'


class AppCreate(AppViewMixin, AppUserObjectMixin, AppFormMixin, CreateView):
    template_name = 'mcoauth/apps/create.html'

    def get_initial(self):
        initial = super(AppCreate, self).get_initial()
        initial['url'] = 'http://'
        initial['redirect_uri'] = 'http://'
        return initial


class AppUpdate(AppViewMixin, AppUserObjectsMixin, AppFormMixin, UpdateView):
    template_name = 'mcoauth/apps/update.html'


class AppDelete(AppViewMixin, AppUserObjectsMixin, AppEditObjectMixin,
                DeleteView):
    template_name = 'mcoauth/apps/delete.html'


class AppCredentials(AppViewMixin, AppUserObjectsMixin, DetailView):
    template_name = 'mcoauth/apps/credentials.html'
