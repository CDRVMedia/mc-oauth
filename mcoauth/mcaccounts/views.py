from django.views.generic import ListView, FormView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, resolve_url

from .models import MinecraftAccount
from .forms import MinecraftAccountForm


class MinecraftList(ListView):
    template_name = 'mcoauth/mcaccounts/list.html'

    def get_queryset(self):
        return MinecraftAccount.objects.filter(user=self.request.user)


class MinecraftCreate(FormView):
    form_class = MinecraftAccountForm
    template_name = 'mcoauth/mcaccounts/create.html'
    success_url = reverse_lazy('minecraft:list')

    def form_valid(self, form):
        form.save(self.request.user)
        return redirect(self.get_success_url())


class MinecraftDelete(DeleteView):
    model = MinecraftAccount
    template_name = 'mcoauth/mcaccounts/delete.html'
    success_url = reverse_lazy('minecraft:list')
