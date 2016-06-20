from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from accounts import const
from braces import views

from .. import forms
from .. import models
from .. import mixins


class LocationListView(mixins.UserMixin, views.LoginRequiredMixin, generic.ListView):
    context_object_name = 'location_list'
    company_template_name = "cowork/locations/company/location_list.html"
    coworker_template_name = "cowork/locations/coworker/location_list.html"

    def get_template_names(self):
        if self.user.user_type == const.USER_TYPE_COMPANY:
            return self.company_template_name
        else:
            return self.coworker_template_name

    def get_queryset(self):
        if self.user.user_type == const.USER_TYPE_COWORKER:
            return models.Desk.objects.filter(owner=self.user)
        else:
            return models.Location.objects.filter(company__user=self.user)

class LocationAddView(mixins.UserMixin, views.LoginRequiredMixin, generic.FormView):
    form_class = forms.LocationCreationForm
    template_name = "cowork/locations/company/location_add.html"
    success_url = reverse_lazy('cowork:locations:list')

    def form_valid(self, form):
        if self.user.companies.count() > 0:
            self.object = form.save(commit=False)
            self.object.company = self.user.companies.first()
            self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
class RentDeskView(mixins.UserMixin, views.LoginRequiredMixin, generic.FormView):
    template_name = "cowork/locations/coworker/location_rent.html"
    success_url = reverse_lazy('cowork:locations:list')
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        rent_form = forms.RentingDeskForm()
        context.update({'rent_form': rent_form})
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        location_id = self.kwargs['pk']
        rent_form = forms.RentingDeskForm(request.POST)
        
        if rent_form.is_valid():
            rent = rent_form.save(commit=False)
            rent.owner = self.user
            rent.location = models.Location.objects.get(id=location_id)
            rent.location.reserve_desk()
            rent.location.save()
            rent.save()
            return HttpResponseRedirect(self.get_success_url())

        context = self.get_context_data(**kwargs)
        context.update({'rent_form': rent_form})
        return self.render_to_response(context)
