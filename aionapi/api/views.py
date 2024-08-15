from .models import User, Business, Team, Employee, Project, Role, Task, UserProjectRole
from .serializers import UserSerializer, UserRegistrationSerializer,UserLoginSerializer, BusinessSerializer, TeamSerializer, EmployeeSerializer, ProjectSerializer, RoleSerializer, TaskSerializer, UserProjectRoleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from datetime import datetime


class UserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user.id,
                'ts': int(datetime.now().timestamp()) # Retrieves in microseconds
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
                user = serializer.validated_data
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': user.id,
                    'ts': int(datetime.now().timestamp()) # Retrieves in microseconds
                }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh_token = request.data.get('rTkn')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Refresh token not provided'}, status=status.HTTP_400_BAD_REQUEST)

class BusinessList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

class TeamList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

class EmployeeList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

class ProjectList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data['owner_id'] = request.user.id  # Assuming the user is authenticated and request.user is available
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            project = serializer.save()
            UserProjectRole.objects.create(user=User.objects.get(id=project.owner_id), project=project, role=Role.objects.get(name='Owner'))            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RoleList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

class TaskList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class UserProjectRoleList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_project_roles = UserProjectRole.objects.all()
        serializer = UserProjectRoleSerializer(user_project_roles, many=True)
        return Response(serializer.data)
    
class UserProjects(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            # Check if the JWT token owner is the same as the user_id provided in the URL
            if request.user.id != user_id:
                return Response({'error': 'Unauthorized access'}, status=status.HTTP_403_FORBIDDEN)

            user_project_roles = UserProjectRole.objects.filter(user_id=user_id)
            project_ids = user_project_roles.values_list('project_id', flat=True)
            projects = Project.objects.filter(id__in=project_ids)
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UsernameSearch(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, search_string):
        try:
            users = User.objects.filter(username__icontains=search_string)
            serializer = UserSerializer(users, many=True)
            usernames = [user['username'] for user in serializer.data]
            return Response(usernames, status=status.HTTP_200_OK)      
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
