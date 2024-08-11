from .models import User, Business, Team, Employee, Project, Role, Task, UserProjectRole
from .serializers import UserRegistrationSerializer,UserLoginSerializer, UserSerializer, BusinessSerializer, TeamSerializer, EmployeeSerializer, ProjectSerializer, RoleSerializer, TaskSerializer, UserProjectRoleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from datetime import datetime
from .encryption import encrypt_token, decrypt_token


class UserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            encrypted_access_token = encrypt_token(str(refresh.access_token))
            encrypted_refresh_token = encrypt_token(str(refresh))
            return Response({
                'refresh': encrypted_refresh_token,
                'access': encrypted_access_token,
                'user': user.id,
                'ts': datetime.now().timestamp()
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
                user = serializer.validated_data
                refresh = RefreshToken.for_user(user)
                encrypted_access_token = encrypt_token(str(refresh.access_token))
                encrypted_refresh_token = encrypt_token(str(refresh))
                return Response({
                    'refresh': encrypted_refresh_token,
                    'access': encrypted_access_token,
                    'user': user.id,
                    'ts': datetime.now().timestamp()
                }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh_token = request.data.get('rTkn')
        if refresh_token:
            try:
                refresh_token = decrypt_token(refresh_token)
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Refresh token not provided'}, status=status.HTTP_400_BAD_REQUEST)

class DecryptJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        encrypted_access_token = request.COOKIES.get('aTkn')
        encrypted_refresh_token = request.COOKIES.get('rTkn')
        if encrypted_access_token:
            try:
                access_token = decrypt_token(encrypted_access_token)
                request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
            except Exception as e:
                return None
        if encrypted_refresh_token:
            try:
                refresh_token = decrypt_token(encrypted_refresh_token)
                request.META['HTTP_REFRESH_TOKEN'] = refresh_token
            except Exception as e:
                return None
        return super().authenticate(request)

class UserList(APIView):
    authentication_classes = [DecryptJWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class BusinessList(APIView):
    authentication_classes = [DecryptJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

class TeamList(APIView):
    authentication_classes = [DecryptJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

class EmployeeList(APIView):
    authentication_classes = [DecryptJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

class ProjectList(APIView):
    authentication_classes = [DecryptJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class RoleList(APIView):
    authentication_classes = [DecryptJWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

class TaskList(APIView):
    authentication_classes = [DecryptJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class UserProjectRoleList(APIView):
    authentication_classes = [DecryptJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_project_roles = UserProjectRole.objects.all()
        serializer = UserProjectRoleSerializer(user_project_roles, many=True)
        return Response(serializer.data)