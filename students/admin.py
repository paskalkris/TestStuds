from django.contrib import admin
from .models import Stud


class StudAdmin(admin.ModelAdmin):
    list_display = ('cgroup', 'nstud', 'name', 'dbirthday')
    list_filter = ['cgroup']

admin.site.register(Stud, StudAdmin)