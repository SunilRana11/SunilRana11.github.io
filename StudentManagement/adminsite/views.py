from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q

# Create your views here.
from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.decorators import login_required
from .forms import Loginform, ResultForm, StudentForm, TeacherForm, noticeForm

from .models import Notice, Result, Teacher, Student
from .filters import *

def home(request):
    results = Result.objects.all()

    context = {
        'results':results
    }

    return render(request,'adminsite/home.html',context)


def about(request):

    return render(request,'adminsite/about.html')


def contact(request):

    return render(request,'adminsite/contact.html')

def why(request):

    return render(request,'adminsite/why.html')

def admission(request):

    return render(request,'adminsite/admission.html')



def adminLogin(request):
    form = Loginform()
    if request.method == 'POST':
        form = Loginform(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')


    context = {
        'form':form
    }

    return render(request,'adminsite/admin_login.html',context)


def logoutAdmin(request):

    logout(request)
    return redirect('home')




@login_required(login_url='login')
def adminDash(request):
    teachers = Teacher.objects.all().count()
    students = Student.objects.all().count()
    notices = Notice.objects.all().count()
    results = Result.objects.all().count() 
    
    context ={
        'noOfTeachers':teachers,
        'noOfStudent': students,
        'notices': notices,
        'results':results,
    }


    return render(request,'adminsite/admin_dash.html',context)



@login_required(login_url='login')
def teacherDash(request):


    teachers = Teacher.objects.all()

    q = request.GET.get('q')
    joinedAfter = request.GET.get('joined-after')
    joinedBefore = request.GET.get('joined-before')
    
    def is_valid_param(param):
        return param != '' and param is not None


    if is_valid_param(q):
        teachers = teachers.filter(name__icontains = q)
    
    if is_valid_param(joinedAfter):
        teachers = teachers.filter(joined_date__gte = joinedAfter)
    if is_valid_param(joinedBefore):
        teachers = teachers.filter(joined_date__lt = joinedBefore)


    context = {
        'teachers':teachers,
    }

    return render(request,'adminsite/teacher_dash.html',context)



@login_required(login_url='login')
def addTeacher(request):

    if request.method == 'POST':
        form = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher-dashboard')
    else:
        form = TeacherForm()

    context = {
        'form':form
    }

    return render(request,'adminsite/add_teacher.html',context)



@login_required(login_url='login')
def editTeacher(request,pk):
    teacher = Teacher.objects.get(id = pk)

    form = TeacherForm(instance= teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher-dashboard')
    

    context = {
        'form':form
    }


    return render(request,'adminsite/edit_teacher.html',context)



@login_required(login_url='login')
def deleteTeacher(request,pk):

    teacher = Teacher.objects.get(id = pk)

    if request.method == 'POST':
        teacher.delete()

        return redirect('teacher-dashboard')

    context = {
        'teacher':teacher
    }

    return render(request,'adminsite/delete.html',context)




@login_required(login_url='login')
def studentDash(request):
    def is_valid_param(param):
        return param != '' and param is not None


    students = Student.objects.all()
    q = request.GET.get('q')
    standard = request.GET.get('standard')
    id = request.GET.get('id')
    if is_valid_param(q):
        multiple_q = Q(Q(name__icontains = q) | Q(address__icontains = q))
        students = students.filter(multiple_q)
    if is_valid_param(standard):
        students =students.filter(standard = standard)
    elif is_valid_param(id):
        students = students.filter(id = id)

    context = {
        'students':students,

    }

    return render(request,'adminsite/student.html',context)

@login_required(login_url='login')
def addStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student-dashboard')

    else:
        form = StudentForm()

    context = {
        'form':form,
    }
    return render(request,'adminsite/add_student.html',context)


@login_required(login_url='login')
def editStudent(request,pk):

    student = Student.objects.get( id = pk)

    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-dashboard')

    context = {
        'form':form
    }

    return render(request,'adminsite/edit_student.html',context)



@login_required(login_url='login')
def deleteStudent(request,pk):
    student = Student.objects.get(id = pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student-dashboard')


    context = {
        'student':student
    }

    return render(request,'adminsite/delete_student.html',context)



@login_required(login_url='login')
def results(request):

    results = Result.objects.all()
    standard = request.GET.get('q')
    batch = request.GET.get('batch')

    
    def is_valid_param(param):
        return param != '' and param is not None


    if is_valid_param(standard):
        results = results.filter(title__icontains = standard)
    if is_valid_param(batch):
        results = results.filter(batch__icontains = batch)

 
    if request.method == 'POST':
        form = ResultForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form = ResultForm()


    context = {
        'form':form,
        "results":results
    }

    return render(request,'adminsite/result.html',context)



def viewresults(request,pk):

    result = Result.objects.get( id = pk)
    form = TeacherForm(request.POST,instance= result)

    context = {
        'result':result,
        'form':form,
    }

    return render(request, 'adminsite/viewresult.html',context)

@login_required(login_url='login')
def deleteresults(request,pk):

    result = Result.objects.get(id = pk)


    if request.method == 'POST':

        result.delete()
        return redirect('/result')

    context = {
        'result':result
    }

    return render(request,'adminsite/delete-result.html',context)

    

@login_required(login_url='login')
def notice(request):

    notices = Notice.objects.all()

    if request.method == 'POST':
        form = noticeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notice')
    else: 
        form = noticeForm()

    context = {
        'form':form,
        'notices':notices
    }

    return render(request,'adminsite/notice.html',context)


def viewnotice(request,pk):

    notice = Notice.objects.get( id = pk)
    form = TeacherForm(instance= Notice)

    context = {
        'notice':notice,
        'form':form,
    }

    return render(request, 'adminsite/viewnotice.html',context)

@login_required(login_url='login')
def deletenotice(request,pk):

    notice = Notice.objects.get(id = pk)


    if request.method == 'POST':

        notice.delete()
        return redirect('/notice')

    context = {
        'notice':notice
    }

    return render(request,'adminsite/delete-notice.html',context)

