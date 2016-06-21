from django.views.generic import TemplateView
from authtools.views import LoginRequiredMixin
from django.shortcuts import render
from accounts import const

from . import mixins
from . import models


class DashboardView(mixins.UserMixin, LoginRequiredMixin, TemplateView):
    template_name = 'cowork/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.user.user_type == const.USER_TYPE_COMPANY:
            context['last_locations'] = models.Location.objects.filter(company__user=self.user)[:5]
        else:
            context['last_locations'] = models.Desk.objects.filter(owner=self.user)[:5]
        return context

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 30:
            errors.append('Please enter at most 30 characters.')
        else:
            if 'f' in request.GET:
                f = request.GET['f']
                if f == "display_free":
                    locations = models.Location.objects.filter(city__icontains=q).extra(where=["total_desks-reserved_desks > 0"])
            else:
                locations = models.Location.objects.filter(city__icontains=q)
            return render(request, 'cowork/search.html', {'locations': locations, 'query': q}) 
    return render(request, 'cowork/search.html', {'errors': errors})
