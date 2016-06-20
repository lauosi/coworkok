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
        return context


##class SearchView(TemplateView):
##    template_name = 'cowork/search.html'
##    model = models.Location
##    
##    def get_context_data(self, request, **kwargs):
##        q = request.GET['q']
##        context = super(SearchView, self).get_context_data(**kwargs)
##        if args:
##            context['locations'] = models.Location.objects.filter(city__icontains=q)
##        return context
       

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 30:
            errors.append('Please enter at most 30 characters.')
        else:
            locations = models.Location.objects.filter(city__icontains=q)
            return render(request, 'cowork/search.html', {'locations': locations, 'query': q}) 
    return render(request, 'cowork/search.html', {'errors': errors})
