from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'mcoauth/core/home.html'


class Dashboard(TemplateView):
    template_name = 'mcoauth/core/dashboard.html'
