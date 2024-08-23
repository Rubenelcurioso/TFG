"""
URL configuration for aionapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from api.views import  UserBusiness, UserDetail, ProjectUsers, UsernameSearch, UserProjects, UserLogout, UserRegistration, UserLogin, BusinessList, TeamList, EmployeeList, ProjectList, RoleList, TaskList, UserProjectRoleList
urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'), # Sign up session
    path('login/', UserLogin.as_view(), name='login'), # Log in session
    path('logout/', UserLogout.as_view(), name='logout'), # Log out session
    path('business/<int:business_id>/', BusinessList.as_view(), name='business-list'), # Get business
    path('business/<int:business_id>/employees/', EmployeeList.as_view(), name='employee-business'), # Get employees from business
    path('business/<int:business_id>/teams/', TeamList.as_view(), name='team-business'), # Get team from business
    path('employees/<int:business_id>/<int:team_id>/', EmployeeList.as_view(), name='employee-list'), # Get employees of the given business and id
    path('new/project/', ProjectList.as_view(), name='new-project'), # New project
    path('new/business/', BusinessList.as_view(), name='new-business'), # New business
    path('new/team/', TeamList.as_view(), name='new-team'), # New team
    path('new/task/', TaskList.as_view(), name='new-task'), # New task
    path('new/employee/', EmployeeList.as_view(), name='new-task'), # New task
    path('new/member/', EmployeeList.as_view(), name='new-team-member'), # New member to the team
    path('team/<int:business_id>/<int:team_id>/', TeamList.as_view(), name='get-team'), # Get team
    path('team/update/', TeamList.as_view(), name='update-team'), # Update team
    path('task/<int:task_id>/', TaskList.as_view(), name='get-task'), # Get task
    path('update/task/<int:task_id>/', TaskList.as_view(), name='update-task'), # Update task
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Token JWT refresh
    path('user/<int:user_id>/projects/', UserProjects.as_view(), name='user-projects'), # Projects of user
    path('user/<int:user_id>/businesses/', UserBusiness.as_view(), name='user-projects'), # Businesses of user
    path('user/<int:user>/', UserDetail.as_view(), name='username-search'), # Search for username given ID
    path('user/<int:user_id>/tasks/', TaskList.as_view(), name='user-tasks'), # User tasks
    path('username/<str:username>/', UsernameSearch.as_view(), name='username-search'), # Search for username
    path('employees/username/<int:business_id>/<str:username>/', UsernameSearch.as_view(), name='employee-username-search'), # Search for username by employees
    path('project/<int:project_id>/', ProjectList.as_view(), name='project'), # Project data
    path('project/<int:project_id>/users/', ProjectUsers.as_view(), name='project-users'), # Users of a project
    path('project/<int:project_id>/teams/', TeamList.as_view(), name='project-teams'), # Teams of a project
    path('project/<int:project_id>/tasks/', TaskList.as_view(), name='project-tasks'), # Tasks of a project
    path('remove/project/<int:project_id>/', ProjectList.as_view(), name='remove-project'), # Remove project
    path('remove/business/<int:business_id>/', BusinessList.as_view(), name='remove-business'), # Remove business
    path('remove/task/<int:task_id>/', TaskList.as_view(), name='remove-task'), # Remove task
    path('remove/employee/<int:business_id>/<str:username>/', EmployeeList.as_view(), name='remove-employee'), # Remove employee
    path('remove/team/<int:business_id>/<int:team_id>/', TeamList.as_view(), name='remove-team'), # Remove team
    path('roles/', RoleList.as_view(), name='role-list'), # Get roles
    path('userprojectrole/', UserProjectRoleList.as_view(), name='userprojectrole-list'), # Create UserProjectRole
]
