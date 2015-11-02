from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django import forms
from django.views import generic
from students.models import Stud
from .models import Group

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
            return JsonResponse(data)
        else:
            return response


class GroupsView(AjaxableResponseMixin, CreateView):
    model = Group
    fields = ['name', 'starosta']
    template_name = 'groups/groups_list.html'

    def dispatch(self, *args, **kwargs):
        self.groups_list = Group.objects.order_by('name')
        return super(GroupsView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(GroupsView, self).get_context_data(**kwargs)
        context['groups_list'] = self.groups_list
        context['data_set'] = self.groups_list
        context['set_name'] = 'groups'
        return context

    def get_form(self, form_class=None):
        form = super(GroupsView, self).get_form(form_class)
        form.fields['starosta'].queryset = Stud.objects.filter(cgroup=form.instance.id)
        return form


