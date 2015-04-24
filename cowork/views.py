from django.views.generic import TemplateView
from authtools.views import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'cowork/dashboard.html'
