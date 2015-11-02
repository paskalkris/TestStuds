from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django import forms
from groups.models import Group

from .models import Stud


class AjaxableResponseMixin(object):
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        print(form.errors.as_json())
        if self.request.is_ajax():
            return JsonResponse(form.errors.as_json(), status=400, safe=False)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        try:
            response = super(AjaxableResponseMixin, self).form_valid(form)
        except Exception as e:
            print(e)
        if self.request.is_ajax():
            data = form.cleaned_data
            #{
            #    'pk': self.object.pk,
            #}
            return JsonResponse(data)
        else:
            return response


class StudsView(AjaxableResponseMixin, CreateView):
    model = Stud
    fields = ['name', 'dbirthday', 'cgroup', 'nstud']
    template_name = 'students/studs_list.html'

    def dispatch(self, *args, **kwargs):
        self.group = get_object_or_404(Group, pk=kwargs['group_pk'])
        return super(StudsView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(StudsView, self).get_context_data(**kwargs)
        context['group'] = self.group
        context['data_set'] = self.group.stud_set
        context['set_name'] = 'students'
        return context

    def get_initial(self):
        return {'cgroup': self.group}

    def get_form(self, form_class=None):
        form = super(StudsView, self).get_form(form_class)
        form.fields['cgroup'].widget = forms.HiddenInput()
        return form

