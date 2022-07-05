from . import views
from django.urls import path,include


urlpatterns = [

    path('',views.home,name='home'),

    path('about/',views.about,name='about'),
    path('admission/',views.admission,name='admission'),
    path('contact/',views.contact,name='contact'),
    path('why/',views.why,name='why'),


    path('admin-login/',views.adminLogin,name='login'),
    path('admin-logout/',views.logoutAdmin,name='logout'),
    path('admin-dashboard/',views.adminDash,name='dashboard'),


    path('teacher-dashboard/',views.teacherDash,name='teacher-dashboard'),
    path('add-teacher/',views.addTeacher,name='add-teacher'),
    path('edit-teacher<str:pk>/',views.editTeacher,name='edit-teacher'),
    path('delete-teacher<str:pk>/',views.deleteTeacher,name='delete-teacher'),


    path('student-dashboard/',views.studentDash,name='student-dashboard'),
    path('add-student/',views.addStudent,name='add-student'),
    path('edit-student<str:pk>/',views.editStudent,name='edit-student'),
    path('delete-student<str:pk>/',views.deleteStudent,name='delete-student'),
    

    path('result/',views.results,name='result'),
    path('view-result/<str:pk>',views.viewresults,name='view-result'),
    path('delete-result/<str:pk>',views.deleteresults,name='delete-result'),

    path('notice/',views.notice,name='notice'),
    path('view-notice/<str:pk>',views.viewnotice,name='view-notice'),
    path('delete-notice/<str:pk>',views.deletenotice,name='delete-notice'),

    

]

