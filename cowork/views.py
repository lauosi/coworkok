from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from authtools.views import LoginRequiredMixin
from accounts import const

from . import mixins
from . import models
from cowork.models import Desk
from cowork.serializers import DeskSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class DashboardView(mixins.UserMixin, LoginRequiredMixin, TemplateView):
    template_name = 'cowork/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.user.user_type == const.USER_TYPE_COMPANY:
            context['last_locations'] = models.Location.objects.filter(company__user=self.user)[:5]
        return context


class SearchView(TemplateView):
    template_name = 'cowork/search.html'


class DesksApi(APIView):
    http_method_names  = ['get']

    def get(self, request):
        city = request.GET.get('city', '')
        count = request.GET.get('count', '')
        date_start = request.GET.get('date_start', '')
        date_end = request.GET.get('date_start', '')
        f = dict()
        if city:
            f['location__city__icontains'] = city
        desks = Desk.objects.filter(**f)
        try:
            c = int(count)
        except ValueError:
            c = None
        if c is not None:
            desks = desks[:c]
        data = dict({'desks': []})
        for desk in desks:
            ser = DeskSerializer(desk)
            data['desks'].append(ser.data)
        return JSONResponse(data=data)