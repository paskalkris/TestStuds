from django.contrib import admin
from django.forms import ModelForm
from .models import Group
from students.models import Stud


class GroupAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        self.fields['starosta'].queryset = Stud.objects.filter(cgroup=self.instance.id)


class StudsInline(admin.TabularInline):
    model = Stud
    extra = 3


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    inlines = [StudsInline]
    list_display = ('name', 'starosta')

admin.site.register(Group, GroupAdmin)