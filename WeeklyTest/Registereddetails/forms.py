from django import forms
from django.forms import ModelForm

from .models import userdetails,Course,Batch


Gender_choices = (
    ('','select Gender'),
    ('male','Male'),
    ('female','Female')

)


class RegisterForm(ModelForm):
    class Meta:
        model = userdetails
        fields = ('First_name','Last_name','Gender','Email','Phone','Course','Batch')
        

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['Batch'].queryset=Batch.objects.none()

        '''if 'Course' in self.data:
            try:
                Course_id =int(self.data.get('Course'))
                self.fields['Batch_name'].queryset = Batch.objects.filter(Course_id=Course_id).order_by('Batch_name')
            except(ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['Batch_name'].queryset = self.instance.Course.Batch_set.order_by('Batch_name')'''



        




