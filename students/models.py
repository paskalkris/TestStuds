from django.core.urlresolvers import reverse
from django.db import models
from groups.models import Group


class Stud(models.Model):
    name = models.CharField("ФИО", max_length=128)
    dbirthday = models.DateField("Дата рождения")
    nstud = models.CharField("Студенческий билет", max_length=15, unique=True)
    cgroup = models.ForeignKey(Group, verbose_name="Группа")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stud:studs_list', args=[self.cgroup.pk])