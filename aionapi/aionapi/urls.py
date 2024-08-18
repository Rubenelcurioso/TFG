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
from api.views import  UserDetail, ProjectUsers, UsernameSearch, UserProjects, UserLogout, UserRegistration, UserLogin, BusinessList, TeamList, EmployeeList, ProjectList, RoleList, TaskList, UserProjectRoleList
urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'), # Sign up session
    path('login/', UserLogin.as_view(), name='login'), # Log in session
    path('logout/', UserLogout.as_view(), name='logout'), # Log out session
    path('businesses/', BusinessList.as_view(), name='business-list'),
    path('teams/', TeamList.as_view(), name='team-list'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('new/project/', ProjectList.as_view(), name='new-project'), # New project
    path('roles/', RoleList.as_view(), name='role-list'),
    path('new/task/', TaskList.as_view(), name='new-task'), # New task
    path('remove/task/<int:task_id>/', TaskList.as_view(), name='remove-task'), # Remove task
    path('user-project-roles/', UserProjectRoleList.as_view(), name='user-project-role-list'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Token JWT refresh
    path('user/<int:user_id>/projects/', UserProjects.as_view(), name='user-projects'), # Projects of user
    path('user/<int:user>/', UserDetail.as_view(), name='username-search'), # Search for username given ID
    path('username/<str:username>/', UsernameSearch.as_view(), name='username-search'), # Search for username
    path('project/<int:project_id>/', ProjectList.as_view(), name='project'), # Project data
    path('project/<int:project_id>/users/', ProjectUsers.as_view(), name='project-users'), # Users of a project
    path('project/<int:project_id>/teams/', UsernameSearch.as_view(), name='project-usernames'), # Teams of a project
    path('project/<int:project_id>/tasks/', TaskList.as_view(), name='project-tasks'), # Tasks of a project
]
