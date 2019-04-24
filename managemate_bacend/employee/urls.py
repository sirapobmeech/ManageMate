from django.urls import path
from .views import *

urlpatterns = [
    path('addemployee/', add_employee.as_view(), name='addemployee'),
    path('getemployee/', get_employee_info.as_view(), name='getemployee'),
    path('checkin/', add_checkin.as_view(), name='checkin'),
    path('getcheckin/', get_checkin.as_view(), name='addcheckin'),
    path('addleave/', add_leaveinfo.as_view(), name='addleave'),
    path('getleaveall/', get_leaveall.as_view(), name='getleaveall'),
    path('getleave/', get_leave.as_view(), name='getleave'),
    path('updateleave/', put_leaveinfo.as_view(), name='update'),
    path('getleavebystaffid/', get_leavebystaffid.as_view(), name='getbystaffid'),
    path('addcalendar/', add_calendar.as_view(), name='addcalendar'),
    path('getcalendar/', get_calendar.as_view(), name='getcalendar'),
    path('addproject/', add_project.as_view(),name='addproject'),
    path('getproject/',get_project.as_view(),name='getproject'),
    path('getprojectbystaffid/',get_projectstaffid.as_view(),name='getprojectbystaffid'),
    path('getprojectbyprojectid/',get_projectprojectid.as_view(),name='getprojectbyprojectid'),
    path('putEmployee/',put_employee.as_view(),name='putemployee'),
    path('putJoinProject/',put_joinproject.as_view(),name='putjoinproject'),
    path('deleteuser/',Delete_user.as_view(),name='deleteUser'),
    path('changeProjectStatus/',put_changeStatus.as_view(),name='changeProjectStatus'),
    path('myproject/',get_myproject.as_view(),name='getmyproject'),
    path('Statistic/',get_checkinAndProfile.as_view(),name='getStatistic')


]
