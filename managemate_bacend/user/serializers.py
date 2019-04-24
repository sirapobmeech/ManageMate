from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User
from employee.models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'user_type')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data.pop('user'))


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
