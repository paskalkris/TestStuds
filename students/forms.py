from django.forms import ModelForm, CharField

from .models import Stud

class StudForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudForm, self).__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].widget.attrs['class'] = 'form-control' 

    class Meta:
        model = Stud
        fields = ['name', 'dbirthday', 'nstud', 'cgroup']

