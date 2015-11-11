from django.db import models

class Group(models.Model):
    name = models.CharField("Наименование", max_length=16, unique=True)
    starosta = models.OneToOneField('students.Stud', blank=True, null=True, verbose_name="Староста")

    def __str__(self):
        return self.name
