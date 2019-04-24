from django.db import models
from datetime import datetime
from user.models import User
from django_postgres_unlimited_varchar import UnlimitedCharField


# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    projectID = models.IntegerField(default=0, blank=True)
    first_name_EN = models.CharField(max_length=50, default='')
    last_name_EN = models.CharField(max_length=50, default='')
    first_name_TH = models.CharField(max_length=50, default='')
    last_name_TH = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=70, blank=True)
    role = models.CharField(max_length=50, default='')
    bank_no = models.CharField(max_length=50, default='')
    bank_name = models.CharField(max_length=50, default='')
    tell_no = models.CharField(max_length=50, default='')
    sick_quo = models.IntegerField(default=0, blank=True)
    sick_remain = models.IntegerField(default=0, blank=True)
    annual_quo = models.IntegerField(default=0, blank=True)
    annual_remain = models.IntegerField(default=0, blank=True)
    lwp_quo = models.IntegerField(default=0, blank=True)
    lwp_remain = models.IntegerField(default=0, blank=True)
    personal_quo = models.IntegerField(default=0, blank=True)
    personal_remain = models.IntegerField(default=0, blank=True)
    lfwos_quo = models.IntegerField(default=0, blank=True)
    lfwos_remain = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.first_name_EN + self.last_name_EN


class CheckIn(models.Model):
    staff = models.ForeignKey(Employee, on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=50, default='')
    time = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=50, default='')
    place = models.CharField(max_length=1000, default='')


class LeaveInfo(models.Model):
    staff = models.ForeignKey(Employee, on_delete=models.CASCADE, default='')
    leave_type = models.CharField(max_length=50, default='')
    leave_start_datetime = models.DateTimeField(default=datetime.now, blank=True)
    leave_end_datetime = models.DateTimeField(default=datetime.now, blank=True)
    leave_status = models.CharField(max_length=50, default='')
    leave_comment = models.CharField(max_length=255, default='')
    approved_by = models.CharField(max_length=50, default='')
    leave_file1 = models.ImageField(upload_to='test')


class calendar(models.Model):
    staff = models.ForeignKey(Employee, on_delete=models.CASCADE, default='')
    datetime = models.DateField(blank=True, null=True)
    Month = models.CharField(max_length=50,default='',blank=True)
    date = models.CharField(max_length=50,default='')
    Hours = models.CharField(max_length=50,default='',blank=True)
    Years = models.CharField(max_length=50,default='',blank=True)
    Minutes = models.CharField(max_length=50, default='',blank=True)
    comment = models.CharField(max_length=255, default='')



class project(models.Model) :
    staff = models.CharField(max_length=50,default='',blank=True)
    ProjectName = models.CharField(max_length=50,default='')
    MemberInProject = models.ManyToManyField(Employee)
    Status = models.CharField(max_length=50,default='')
    comment = models.CharField(max_length=255,default='')


