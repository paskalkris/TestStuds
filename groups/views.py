from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django import forms
from django.views import generic
from students.models import Stud
from .models import Group
from .forms import GroupForm


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

@login_required
def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group:groups_list')
    else:
        form = GroupForm()
    return render(request, 'groups/group_form.html', {'form': form})

@login_required
def group_edit(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group:groups_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'groups/group_form.html', {'form': form, 'group': group})

@login_required
def group_delete(request, group_id):
    if request.method == 'POST':
        return
    group = get_object_or_404(Group, pk=group_id)
    try:
        group.delete()
        return redirect('group:groups_list')
    except Exception as e:
        form = GroupForm(instance=group)
        return render(request, 'groups/group_form.html', {'form': form, 'group': group, 'error_message': e})

@login_required
def confirm_delete(request, group_id):
    if request.method == 'POST':
        return
    group = get_object_or_404(Group, pk=group_id)
    context = {'group': group}
    template_name = 'groups/confirm_delete.html'
    return render(request, template_name, context)
