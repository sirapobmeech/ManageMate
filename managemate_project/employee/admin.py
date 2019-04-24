from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    pass


@admin.register(LeaveInfo)
class LeaveInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(project)
class projectAdmin(admin.ModelAdmin):
    pass


class CalendarAdmin(admin.ModelAdmin):
    list_display = ['staff', 'datetime', 'date', 'comment']


admin.site.register(calendar, CalendarAdmin)
