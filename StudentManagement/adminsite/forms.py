from django import forms

from .models import Notice, Result, Teacher, Student




class Loginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
    }))

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

        labels ={
            'name' :'',
            'address' :'',
            'joined_date' :'',
            'contact' :'',
        }


        widgets = {
           'name': forms.TextInput(attrs={
            'class' : 'form-control','placeholder':'Name'
            }),
            'address': forms.TextInput(attrs={
            'class':'form-control','placeholder': 'Enter Address'
            }),
            'joined_date': forms.DateInput(attrs={
                'class':'form-control','placeholder': 'joined date'
            }),
            'contact':forms.TextInput(attrs={
                'class':'form-control','placeholder': 'Contact'
            }),
            'teaches':forms.Select(attrs= {
                'class':'form-control','placeholder': 'Teaches'
            }),

        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'parentsContact': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'standard': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = "__all__"



        widgets = {
           
           'title': forms.TextInput(attrs={
            'class' : 'form-control','placeholder':'Enter Title.....'}),
           'standard': forms.TextInput(attrs={
            'class' : 'form-control','placeholder':'Enter standard..'}),
        
        }

class noticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = "__all__"


        widgets = {
           'title': forms.TextInput(attrs={
            'class' : 'form-control','placeholder':'Enter Title.....'}),
           'description': forms.Textarea(attrs={
            'class' : 'form-control','placeholder':'Enter description..'}),
        
        }

