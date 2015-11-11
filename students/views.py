from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from groups.views import studs_list
from .models import Stud
from .forms import StudForm


def stud_create(request, group_id):
    if request.method == 'POST':
        form = StudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group:studs_list', group_id=group_id)
    else:
        form = StudForm(initial={'cgroup': group_id})
    return render(request, 'students/stud_form.html', {'form': form})


def stud_edit(request, group_id, stud_id):
    stud = get_object_or_404(Stud, pk=stud_id)
    if request.method == 'POST':
        form = StudForm(request.POST, instance=stud)
        if form.is_valid():
            form.save()
            return redirect('group:studs_list', group_id=group_id)
    else:
        form = StudForm(instance=stud)
    return render(request, 'students/stud_form.html', {'form': form, 'stud': stud})


def stud_delete(request, group_id, stud_id):
    stud = get_object_or_404(Stud, pk=stud_id)
    try:
        stud.delete()
        return redirect('group:studs_list', group_id=group_id)
    except Exception as e:
        form = StudForm(instance=stud)
        return render(request, 'students/stud_form.html', {'form': form, 'stud': stud, 'error_message': e})

