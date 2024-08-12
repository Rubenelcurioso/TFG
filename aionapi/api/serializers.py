from rest_framework import serializers
from .models import User, Business, Team, Employee, Project, Role, Task, UserProjectRole
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, get_user_model

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
        # user and user.check_password(password)
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
    class Meta:
        model = Project
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserProjectRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProjectRole
        fields = '__all__'