from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=16, unique=True)
    starosta = models.OneToOneField('students.Stud', blank=True, null=True)

    def __str__(self):
        return self.name
