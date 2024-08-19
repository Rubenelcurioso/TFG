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
                'username': user.username,
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
                    'username': user.username,
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

class UserDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            return Response({'username': user.username}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

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


    def delete(self, request, project_id):
        try:
            project = Project.objects.get(id=project_id)
            if project.owner != request.user:
                return Response({'error': 'You do not have permission to delete this project'}, status=status.HTTP_403_FORBIDDEN)
            
            project.delete()
            return Response({'message': 'Project deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, project_id=None):
        if project_id:
            try:
                project = Project.objects.get(id=project_id)
                if not UserProjectRole.objects.filter(user=request.user, project=project).exists():
                    return Response({'error': 'You do not have access to this project'}, status=status.HTTP_403_FORBIDDEN)
                serializer = ProjectSerializer(project)
            except Project.DoesNotExist:
                return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            user_projects = UserProjectRole.objects.filter(user=request.user).values_list('project', flat=True)
            projects = Project.objects.filter(id__in=user_projects)
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

    def put(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is part of the project
        user_project_role = UserProjectRole.objects.filter(user=request.user, project=task.project).first()
        if not user_project_role:
            return Response({'error': 'You do not have access to this task'}, status=status.HTTP_403_FORBIDDEN)

        # Check if the user role has sufficient permissions
        if user_project_role.role.name == 'Guest' or user_project_role.role.perm < 5:
            return Response({'error': 'You do not have sufficient permissions to edit this task'}, status=status.HTTP_403_FORBIDDEN)

        print(request.data)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is part of the project
        user_project_role = UserProjectRole.objects.filter(user=request.user, project=task.project).first()
        if not user_project_role:
            return Response({'error': 'You do not have access to this task'}, status=status.HTTP_403_FORBIDDEN)

        # Check if the user role is not a guest and has sufficient permissions
        if user_project_role.role.name == 'Guest' or user_project_role.role.perm < 7:
            return Response({'error': 'You do not have sufficient permissions to delete this task'}, status=status.HTTP_403_FORBIDDEN)

        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, project_id=None, task_id=None, user_id=None):
        if task_id:
            try:
                task = Task.objects.select_related('user_assigned', 'team_assigned', 'project').get(id=task_id)
            except Task.DoesNotExist:
                return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

            # Check if the user has access to the project
            user_project_role = UserProjectRole.objects.filter(user=request.user, project=task.project).first()
            if not user_project_role:
                return Response({'error': 'You do not have access to this task'}, status=status.HTTP_403_FORBIDDEN)

            task_info = {
                'id': task.id,
                'name': task.name,
                'description': task.description,
                'user': task.user_assigned.username if task.user_assigned else None,
                'priority': task.get_priority_display(),
                'start_date': task.start_date,
                'end_date': task.end_date,
                'status': task.get_status_display(),                
                'team': task.team_assigned.name if task.team_assigned else None
            }
            return Response(task_info)
        
        elif project_id:
            # Check if the user has access to the project
            user_project_role = UserProjectRole.objects.filter(user=request.user, project_id=project_id).first()
            if not user_project_role:
                return Response({'error': 'You do not have access to this project'}, status=status.HTTP_403_FORBIDDEN)
            
            tasks = Task.objects.filter(project_id=project_id).select_related('user_assigned', 'team_assigned')
            
            task_data = []
            for task in tasks:
                task_info = {
                    'id': task.id,
                    'name': task.name,
                    'description': task.description,
                    'user': task.user_assigned.username if task.user_assigned else None,
                    'priority': task.get_priority_display(),
                    'start_date': task.start_date,
                    'end_date': task.end_date,
                    'status': task.get_status_display(),                
                    'team': task.team_assigned.name if task.team_assigned else None
                }
                task_data.append(task_info)
            
            return Response(task_data)
        
        elif user_id:
            # Get tasks for the user making the request
            tasks = Task.objects.filter(user_assigned=request.user).select_related('user_assigned', 'team_assigned', 'project')
            
            task_data = []
            for task in tasks:
                task_info = {
                    'id': task.id,
                    'name': task.name,
                    'description': task.description,
                    'user': task.user_assigned.username,
                    'priority': task.get_priority_display(),
                    'start_date': task.start_date,
                    'end_date': task.end_date,
                    'status': task.get_status_display(),                
                    'team': task.team_assigned.name if task.team_assigned else None,
                    'project': task.project.name
                }
                task_data.append(task_info)
            
            return Response(task_data)
        
    def post(self, request):
        # Check if the user has sufficient permissions
        user_project_role = UserProjectRole.objects.filter(user=request.user, project_id=request.data.get('project')).first()
        if not user_project_role or user_project_role.role.perm < 7:
            return Response({'error': 'You do not have sufficient permissions to create a task'}, status=status.HTTP_403_FORBIDDEN)

        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

            user_project_roles = UserProjectRole.objects.filter(user_id=user_id).select_related('role', 'project')
            projects_data = []
            for upr in user_project_roles:
                project_data = ProjectSerializer(upr.project).data
                project_data['role_perm'] = upr.role.perm if upr.role else None
                projects_data.append(project_data)
            
            return Response(projects_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProjectUsers(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, project_id):
        try:
            # Check if the user has access to the project
            if not UserProjectRole.objects.filter(user=request.user, project_id=project_id).exists():
                return Response({'error': 'Unauthorized access'}, status=status.HTTP_403_FORBIDDEN)

            user_project_roles = UserProjectRole.objects.filter(project_id=project_id)
            user_ids = user_project_roles.values_list('user_id', flat=True)
            users = User.objects.filter(id__in=user_ids)
            serializer = UserSerializer(users, many=True)
            user_data = [{'id': user['id'], 'username': user['username']} for user in serializer.data]
            return Response(user_data, status=status.HTTP_200_OK)
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
