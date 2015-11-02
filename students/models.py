from django.core.urlresolvers import reverse
from django.db import models
from groups.models import Group


class Stud(models.Model):
    name = models.CharField(max_length=128)
    dbirthday = models.DateField()
    nstud = models.CharField(max_length=15, unique=True)
    cgroup = models.ForeignKey(Group)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stud:studs_list', args=[self.cgroup.pk])