
from Users.models import Student

from django.forms import ModelForm

class User_Form(ModelForm):

    class Meta():
        model = Student
        fields="__all__"

