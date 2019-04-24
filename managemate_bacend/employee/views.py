from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import GetEmployeeInfoSerializer, GetCheckinInfoSerializer, GetLeaveAllSerializer, \
    GetLeaveDetailSerializer, GetStaffLeaveSerializer, GetCalendarSerializer, GetProjectSerializer
from user.models import User
from user.serializers import UserSerializer
import dateutil.parser


# Create your views here.

class add_employee(APIView):
    def post(self, request):
        print(request.data['user'])
        serializer = UserSerializer(data=request.data['user'])
        if serializer.is_valid(raise_exception=ValueError):
            user_obj = serializer.create(validated_data=request.data)
        p = Employee(
            user=user_obj,
            projectID=request.data['data']['projectID'],
            first_name_EN=request.data['data']['firstnameEN'],
            last_name_EN=request.data['data']['lastnameEN'],
            first_name_TH=request.data['data']['firstnameTH'],
            last_name_TH=request.data['data']['lastnameTH'],
            email=request.data['data']['email'],
            role=request.data['data']['role'],
            bank_no=request.data['data']['bankNO'],
            bank_name=request.data['data']['bankName'],
            tell_no=request.data['data']['tellNO'],
            sick_quo=request.data['data']['sickQuo'],
            sick_remain=request.data['data']['sickQuo'],
            annual_quo=request.data['data']['annualQuo'],
            annual_remain=request.data['data']['annualQuo'],
            lwp_quo=request.data['data']['lwpQuo'],
            lwp_remain=request.data['data']['lwpQuo'],
            personal_quo=request.data['data']['personalQuo'],
            personal_remain=request.data['data']['personalQuo'],
            lfwos_quo=request.data['data']['lfwosQuo'],
            lfwos_remain=request.data['data']['lfwosQuo']
        )
        p.save()
        return Response(status=status.HTTP_201_CREATED)


class get_employee_info(APIView):
    def get(self, request):
        employee_info_list = Employee.objects.all().order_by('id')
        serializers = GetEmployeeInfoSerializer(employee_info_list, many=True)
        return Response(serializers.data)


class add_checkin(APIView):
    def post(self, request):
        print(request.data)
        if CheckIn.objects.filter(date=request.data['date'], status=request.data['status'],staff__id=request.data['staffID']):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            if request.data['status'] == "out":
                if CheckIn.objects.filter(date=request.data['date'], status='in',staff__id=request.data['staffID']):
                    print(1)
                    p = CheckIn(
                        staff=get_object_or_404(Employee, id=request.data['staffID']),
                        date=request.data['date'],
                        time=request.data['time'],
                        status=request.data['status'],
                        place=request.data['place'],
                    )
                    p.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                p = CheckIn(
                    staff=get_object_or_404(Employee, id=request.data['staffID']),
                    date=request.data['date'],
                    time=request.data['time'],
                    status=request.data['status'],
                    place=request.data['place'],
                )
                p.save()
            return Response(status=status.HTTP_201_CREATED)

class get_leaveall(APIView):
    def get(self, request):
        LeaveInfo_list = LeaveInfo.objects.all()
        serializers = GetLeaveAllSerializer(LeaveInfo_list, many=True)
        return Response(serializers.data)


# class add_checkout(APIView):
#     def post(self,request):
#         # pass
#         if CheckIn.objects.filter(date=request.data['date'],status='checkin'):
#
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


class get_checkin(APIView):
    def get(self, request):
        print(request.GET.get('staffId'))
        if request.GET.get('staffId'):
            staffId = request.GET.get('staffId')
        checkins = CheckIn.objects.filter(staff__id=staffId)
        serializers = GetCheckinInfoSerializer(checkins, many=True)
        return Response(serializers.data)


class add_leaveinfo(APIView):
    def post(self, request):
        print("bas")

        if request.data['leaveFile1'] == '':
            p = LeaveInfo(
                staff=get_object_or_404(Employee, id=request.data['staffID']),
                leave_type=request.data['leaveType'],
                leave_start_datetime=request.data['leaveStartDateTime'],
                leave_end_datetime=request.data['leaveEndDateTime'],
                leave_status=request.data['leaveStatus'],
                leave_comment=request.data['leaveComment'],
                approved_by=request.data['approvedBy'],
            )
        else:
            import base64
            from django.core.files.base import ContentFile
            # name = request.data['firstnameEN']+request.data['lastnameEN']+str(request.data["staffID"])
            image64 = request.data['leaveFile1']
            print(request.data['leaveFile1'])
            format, imagstr = image64.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imagstr), name='staff.' + ext)
            p = LeaveInfo(
                staff=get_object_or_404(Employee, id=request.data['staffID']),
                leave_type=request.data['leaveType'],
                leave_start_datetime=request.data['leaveStartDateTime'],
                leave_end_datetime=request.data['leaveEndDateTime'],
                leave_status=request.data['leaveStatus'],
                leave_comment=request.data['leaveComment'],
                approved_by=request.data['approvedBy'],
                leave_file1=data
            )
        p.save()

        # p.leave_file1.save(data, save=True)
        # print(image)
        # p.leave_file1.save('1111',image,save=True)
        return Response(status=status.HTTP_201_CREATED)


class get_leaveall(APIView):
    def get(self, request):
        LeaveInfo_list = LeaveInfo.objects.all().order_by('id')
        serializers = GetLeaveAllSerializer(LeaveInfo_list, many=True)
        return Response(serializers.data)


class get_leave(APIView):
    def get(self, request):
        # print(1)
        if request.GET.get('leaveId'):
            leaveId = request.GET.get('leaveId')
            # print(leaveId)
        LeaveInfo_list = LeaveInfo.objects.filter(id=leaveId).order_by('id')
        serializers = GetLeaveDetailSerializer(LeaveInfo_list, many=True, context={"request": request})
        return Response(serializers.data)


class get_leavebystaffid(APIView):
    def get(self, request):
        if request.GET.get('staffId'):
            staffId = request.GET.get('staffId')
        leaveinfo = LeaveInfo.objects.filter(staff__id=staffId).order_by('id')
        serializers = GetStaffLeaveSerializer(leaveinfo, many=True)
        return Response(serializers.data)


class put_leaveinfo(APIView):
    def post(self, request):
        print(request.data)

        if LeaveInfo.objects.filter(id=request.data['leaveId']) and request.data['status'] == 'Approved':
            leave_id = get_object_or_404(LeaveInfo, id=request.data['leaveId'])
            diff = (leave_id.leave_end_datetime - leave_id.leave_start_datetime)
            diffDay = int(diff.days)
            print(diffDay)
            if diffDay == 0:
                diffDay = 0
            employee_id = get_object_or_404(Employee, id=leave_id.staff.id)
            if leave_id.leave_type == "SICK LEAVE":
                employee_id.sick_remain = employee_id.sick_remain - (diffDay+1)
                if employee_id.sick_remain < 0:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    employee_id.save()
            elif leave_id.leave_type == "ANNUAL LEAVE":
                employee_id.annual_remain = employee_id.annual_remain - (diffDay+1)
                if employee_id.annual_remain < 0:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    employee_id.save()
            elif leave_id.leave_type == "LEAVE WITH OUT PAY":
                employee_id.lwp_remain = employee_id.lwp_remain - (diffDay+1)
                if employee_id.lwp_remain < 0:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    employee_id.save()
            elif leave_id.leave_type == "PERSONAL LEAVE":
                employee_id.personal_remain = employee_id.personal_remain - (diffDay+1)
                if employee_id.personal_remain < 0:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    employee_id.save()
            elif leave_id.leave_type == "LEAVE FOR WORK OUTSIDE":
                employee_id.lfwos_remain = employee_id.lfwos_remain - (diffDay+1)
                if employee_id.lfwos_remain < 0:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    employee_id.save()
        LeaveInfo.objects.filter(id=request.data['leaveId']).update(leave_status=request.data['status'],
                                                                    approved_by=request.data['approverId'])
        return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class add_calendar(APIView):
    def post(self, request):
        import datetime
        # print(datetime.datetime.strptime(request.data['datetime'], "%Y-%m-%d").date())
        # print(type(datetime.datetime.strptime(request.data['datetime'], "%Y-%m-%d").date()))
        p = calendar(
            staff=get_object_or_404(Employee, id=request.data['staffID']),
            datetime=datetime.datetime.strptime(request.data['datetime'], "%Y-%m-%d").date(),
            Month=request.data['Month'],
            date=request.data['date'],
            Hours=request.data['Hours'],
            Minutes=request.data['Minutes'],
            comment=request.data['comment'],
            Years=request.data['Years']
        )
        p.save()
        return Response(status=status.HTTP_201_CREATED)


class get_calendar(APIView):
    def get(self, request):
        calendar_list = calendar.objects.all()
        serializers = GetCalendarSerializer(calendar_list, many=True)
        return Response(serializers.data)


class add_project(APIView):
    def post(self, request):
        p = project(
            staff=get_object_or_404(Employee, id=request.data['staffID']),
            ProjectName=request.data['ProjectName'],
            Status=request.data['Status'],
            comment=request.data['Comment'],
        )
        p.save()
        return Response(status=status.HTTP_201_CREATED)


class get_project(APIView):
    def get(self, request):
        project_list = project.objects.all().order_by('id')
        serializers = GetProjectSerializer(project_list, many=True)
        return Response(serializers.data)


class get_projectstaffid(APIView):
    def get(self, request):
        if request.GET.get('staffId'):
            staffIds = request.GET.get('staffId')
        projects = project.objects.filter(staff__id=staffIds).order_by('id')
        serializers = GetProjectSerializer(projects, many=True)
        return Response(serializers.data)


class get_projectprojectid(APIView):
    def get(self, request):
        if request.GET.get('projectId'):
            projectId = request.GET.get('projectId')
        projects = project.objects.filter(id=projectId)
        serializers = GetProjectSerializer(projects, many=True)
        return Response(serializers.data)


class put_employee(APIView):
    def post(self, request):
        print(request.data['lfwosQuo'])
        employee = get_object_or_404(Employee, id=request.data['staffId'])
        employee.first_name_EN = request.data['firstnameEN']
        employee.last_name_EN = request.data['lastnameEN']
        employee.email = request.data['email']
        # employee.tell_no = request.data['telNo']
        employee.bank_no = request.data['bankNo']
        employee.bank_name = request.data['bankName']
        employee.sick_quo = request.data['sickQuo']
        employee.sick_remain = request.data['sickRemain']
        employee.annual_quo = request.data['annualQuo']
        employee.annual_remain = request.data['annualRemain']
        employee.lwp_quo = request.data['lwpQuo']
        employee.lwp_remain = request.data['lwpRemain']
        employee.personal_quo = request.data['personalQuo']
        employee.personal_remain = request.data['personalRemain']
        employee.lfwos_quo = request.data['lfwosQuo']
        employee.lfwos_remain = request.data['lfwosRemain']
        employee.save()


class put_joinproject(APIView):
    def post(self, request):
        print(request.data['projectID'])
        getproject = get_object_or_404(project, id=request.data['projectID'])
        getproject.MemberInProject.add(get_object_or_404(Employee, id=request.data['staffId']))
        # getproject.save()
        return Response(status=status.HTTP_200_OK)


class Delete_user(APIView):
    def post(self, request):
        # if Employee.objects.filter(id=request.data['staffId']).delete():
        if Employee.objects.filter(id=request.data['staffId']):
            staff=get_object_or_404(Employee,id=request.data['staffId'])
            staff.user.delete()
            staff.delete()
            # user = Employee.objects.filter(id=request.data['staffId'])
            # user.user.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class put_changeStatus(APIView):
    def post(self, request):
        project.objects.filter(id=request.data['projectID']).update(Status=request.data['status'])


class get_myproject(APIView):
    def get(self, request):
        if request.GET.get('staffId'):
            staffId = request.GET.get('staffId')
        print(staffId)
        projects = project.objects.filter(MemberInProject__id=staffId)
        print(projects)
        serializers = GetProjectSerializer(projects, many=True)
        # print(serializers)
        return Response(serializers.data)

class get_checkinAndProfile(APIView):
    def get(self, request):

        if request.GET.get('staffId'):
            staffId = int(request.GET.get('staffId'))
        checkins = CheckIn.objects.filter(staff__id=staffId)
        profiles = Employee.objects.filter(id=staffId)
        serializers = GetCheckinInfoSerializer(checkins, many=True)
        serializers2 = GetEmployeeInfoSerializer(profiles,many=True)
        return Response({
            '1':serializers.data,
            '2':serializers2.data})








