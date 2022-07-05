import django_filters
from django_filters import DateFilter

from .models import *

class StudentFilter(django_filters.FilterSet):

    class Meta: 
        model = Student
        fields = {
            'standard':['icontains'],
        }
class TeacherFilter(django_filters.FilterSet):


    class Meta:
        model = Teacher
        fields = {
            'joined_date':['icontains'],
        }
