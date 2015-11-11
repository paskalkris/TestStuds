from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django import forms
from django.views import generic
from students.models import Stud
from .models import Group
from .forms import GroupCreateForm, GroupEditForm


def groups_list(request):
    glist = Group.objects.order_by('name')
    context = {'groups_list': glist}
    template_name = 'groups/groups_list.html'
    return render(request, template_name, context)


def studs_list(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    context = {'group': group}
    template_name = 'groups/studs_list.html'
    return render(request, template_name, context)


def group_create(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group:groups_list')
    else:
        form = GroupCreateForm()
    return render(request, 'groups/group_form.html', {'form': form})


def group_edit(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupEditForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group:groups_list')
    else:
        form = GroupEditForm(instance=group)
    return render(request, 'groups/group_form.html', {'form': form, 'group': group})


def group_delete(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    try:
        group.delete()
        return redirect('group:groups_list')
    except Exception as e:
        form = GroupEditForm(instance=group)
        return render(request, 'groups/group_form.html', {'form': form, 'group': group, 'error_message': e})


def confirm_delete(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    context = {'group': group}
    template_name = 'groups/confirm_delete.html'
    return render(request, template_name, context)