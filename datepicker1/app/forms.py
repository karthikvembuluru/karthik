# datetimepicker_app/forms.py
from django import forms
from .models import SelectedDate,Task,User,SelectedTime


class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}

class DateForm(forms.ModelForm):
    class Meta:
        model = SelectedDate
        fields = ['selected_date']
        widgets = {
            'selected_date': forms.DateInput(attrs={'type': 'date'})
        }
        

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [ 'title','time','description', 'completed']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }