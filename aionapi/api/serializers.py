from rest_framework import serializers
from .models import User, Business, Team, Employee, Project, Role, Task, UserProjectRole
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, get_user_model
import re

AuthUser = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = User.objects.filter(username=username).first()
        user = authenticate(username=username, password=password)
        if user:
            return user
        else:
            raise serializers.ValidationError('Invalid credentials')


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'fullname', 'birthday', 'phone', 'password', 'password2']

    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({'username': 'Username already exists'})
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        AuthUser.objects.create_user(username=user.username, password=validated_data['password'], is_superuser=False, is_staff=False)        
        return user


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Project
        fields = '__all__'

    def validate(self, data):
        if data['start_date'] and data['end_date'] and data['start_date'] > data['end_date']:
            raise serializers.ValidationError("Start date must be before or equal to end date.")
        if not re.match("^[A-Za-z0-9 ]*$", data['name']):
            raise serializers.ValidationError("Project name must contain only numbers, spaces, and letters.")
        return data
    
    def create(self, validated_data):
        owner_id = validated_data.pop('owner_id')
        owner = User.objects.get(id=owner_id)
        project = Project.objects.create(owner=owner, **validated_data)
        return project
    
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def to_internal_value(self, data):
        # Convert priority
        priority_mapping = {'LOW': 'L', 'MEDIUM': 'M', 'HIGH': 'H'}
        if 'priority' in data:
            data['priority'] = priority_mapping.get(data['priority'].upper(), data['priority'])
        
        # Convert status
        status_mapping = {
            'todo': 'TODO', 
            'to do': 'TODO',
            'in progress': 'IN_PROGRESS',
            'inprogress': 'IN_PROGRESS',
            'in_progress': 'IN_PROGRESS',
            'done': 'DONE'
        }
        if 'status' in data:
            data['status'] = status_mapping.get(data['status'].lower(), data['status'])
        return super().to_internal_value(data)
    def validate(self, data):
        if data.get('start_date') and data.get('end_date') and data['start_date'] > data['end_date']:
            raise serializers.ValidationError("Start date must be before end date.")

        return data
class UserProjectRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProjectRole
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_username(self, value):
        if not re.match("^[A-Za-z0-9]*$", value):
            raise serializers.ValidationError("Username must contain only numbers and letters.")
        return value
