from django.forms import ModelForm

from students.models import Stud
from .models import Group

class GroupForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['starosta'].queryset = Stud.objects.filter(cgroup=self.instance.id)
        for name in self.fields:
            self.fields[name].widget.attrs['class'] = 'form-control'


    class Meta:
        model = Group
        fields = ['name', 'starosta']
