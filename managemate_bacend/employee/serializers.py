from rest_framework import serializers
from .models import Employee, CheckIn, LeaveInfo, calendar, project
from django_postgres_unlimited_varchar import UnlimitedCharField


class GetEmployeeInfoSerializer(serializers.ModelSerializer):
    staffID = serializers.IntegerField(source='id')
    firstnameEN = serializers.CharField(source='first_name_EN')
    lastnameEN = serializers.CharField(source='last_name_EN')
    firstnameTH = serializers.CharField(source='first_name_TH')
    lastnameTH = serializers.CharField(source='last_name_TH')
    bankNo = serializers.CharField(source='bank_no')
    bankName = serializers.CharField(source='bank_name')
    tellno = serializers.CharField(source='tell_no')
    sickQuo = serializers.IntegerField(source='sick_quo')
    sickRemain = serializers.IntegerField(source='sick_remain')
    annualQuo = serializers.IntegerField(source='annual_quo')
    annualRemain = serializers.IntegerField(source='annual_remain')
    lwpQuo = serializers.IntegerField(source='lwp_quo')
    lwpRemain = serializers.IntegerField(source='lwp_remain')
    personalQuo = serializers.IntegerField(source='personal_quo')
    personalRemain = serializers.IntegerField(source='personal_remain')
    lfwosQuo = serializers.IntegerField(source='lfwos_quo')
    lfwosRemain = serializers.IntegerField(source='lfwos_remain')

    class Meta:
        model = Employee
        fields = ('staffID', 'projectID', 'firstnameEN', 'lastnameEN', 'firstnameTH',
                  'lastnameTH', 'email', 'role', 'bankNo', 'bankName', 'tellno', 'sickQuo', 'sickRemain',
                  'annualQuo', 'annualRemain', 'lwpQuo', 'lwpRemain', 'personalQuo', 'personalRemain',
                  'lfwosQuo', 'lfwosRemain')


class GetCheckinInfoSerializer(serializers.ModelSerializer):
    staffID = serializers.IntegerField(source='staff.id')
    Date = serializers.CharField(source='date')
    Time = serializers.CharField(source='time')
    Status = serializers.CharField(source='status')

    class Meta:
        model = CheckIn
        fields = ('staffID', 'Date', 'Time', 'Status', 'place')


class GetLeaveDetailSerializer(serializers.ModelSerializer):
    StaffID = serializers.IntegerField(source='staff.id')
    LeaveID = serializers.IntegerField(source='id')
    FirstnameEN = serializers.CharField(source='staff.first_name_EN')
    LastnameEN = serializers.CharField(source='staff.last_name_EN')
    LeaveStatus = serializers.CharField(source='leave_status')
    Role = serializers.CharField(source='staff.role')
    approvedBy = serializers.CharField(source='approved_by')
    LeaveStartDateTime = serializers.DateTimeField(source='leave_start_datetime')
    LeaveEndDateTime = serializers.DateTimeField(source='leave_end_datetime')
    LeaveComment = serializers.CharField(source='leave_comment')
    LeaveFile1 = serializers.ImageField(source='leave_file1')
    LeaveType = serializers.CharField(source='leave_type')

    class Meta:
        model = LeaveInfo
        fields = (
            'LeaveID', 'FirstnameEN', 'LastnameEN', 'Role', 'LeaveStatus', 'approvedBy', 'LeaveStartDateTime',
            'LeaveEndDateTime', 'LeaveComment', 'StaffID',
            'LeaveFile1', 'LeaveType')


class GetLeaveAllSerializer(serializers.ModelSerializer):
    leaveID = serializers.IntegerField(source='id')
    firstnameEN = serializers.CharField(source='staff.first_name_EN')
    lastnameEN = serializers.CharField(source='staff.last_name_EN')
    leaveStatus = serializers.CharField(source='leave_status')
    approvedBy = serializers.CharField(source='approved_by')
    LeaveStartDateTime = serializers.DateTimeField(source='leave_start_datetime')

    class Meta:
        model = LeaveInfo
        fields = (
            'leaveID', 'firstnameEN', 'lastnameEN', 'leaveStatus', 'approvedBy', 'LeaveStartDateTime')


class GetStaffLeaveSerializer(serializers.ModelSerializer):
    StaffID = serializers.IntegerField(source='staff.id')
    leaveID = serializers.IntegerField(source='id')
    firstnameEN = serializers.CharField(source='staff.first_name_EN')
    lastnameEN = serializers.CharField(source='staff.last_name_EN')
    leaveStatus = serializers.CharField(source='leave_status')
    Role = serializers.CharField(source='staff.role')
    approvedBy = serializers.CharField(source='approved_by')
    LeaveStartDateTime = serializers.DateTimeField(source='leave_start_datetime')
    LeaveEndDateTime = serializers.DateTimeField(source='leave_end_datetime')
    LeaveComment = serializers.CharField(source='leave_comment')
    LeaveFile1 = serializers.ImageField(source='leave_file1')
    LeaveType = serializers.CharField(source='leave_type')

    class Meta:
        model = LeaveInfo
        fields = (
            'leaveID', 'firstnameEN', 'lastnameEN', 'Role', 'leaveStatus', 'approvedBy', 'LeaveStartDateTime',
            'LeaveEndDateTime', 'LeaveComment', 'StaffID',
            'LeaveFile1', 'LeaveType')


class GetCalendarSerializer(serializers.ModelSerializer):
    staffId = serializers.IntegerField(source='staff.id')
    FirstnameEN = serializers.CharField(source='staff.first_name_EN')
    LastnameEN = serializers.CharField(source='staff.last_name_EN')

    class Meta:
        model = calendar
        fields = (
            'staffId', 'datetime', 'date', 'comment', 'FirstnameEN', 'LastnameEN', 'Month', 'Hours', 'Minutes','Years'
        )


class GetProjectSerializer(serializers.ModelSerializer):
    projectID = serializers.IntegerField(source='id')
    Staffname = serializers.CharField(source='staff')
    ProjectDetail = serializers.CharField(source='comment')
    MemberInProject = serializers.SerializerMethodField('get_member_name')

    class Meta:
        model = project
        fields = (
            'projectID', 'ProjectName', 'Staffname', 'comment', 'Status', 'ProjectDetail', 'MemberInProject'
        )

    def get_member_name(self, obj):
        try:
            member_name = []
            project_obj = project.objects.get(id=obj.id)
            for name in project_obj.MemberInProject.all():
                member_name.append(name.first_name_EN)
            return member_name
        except:
            return 'query error'
