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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import UsernameSearch, UserProjects, UserLogout, UserRegistration, UserLogin, BusinessList, TeamList, EmployeeList, ProjectList, RoleList, TaskList, UserProjectRoleList
urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('businesses/', BusinessList.as_view(), name='business-list'),
    path('teams/', TeamList.as_view(), name='team-list'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('new/project/', ProjectList.as_view(), name='project-list'),
    path('roles/', RoleList.as_view(), name='role-list'),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('user-project-roles/', UserProjectRoleList.as_view(), name='user-project-role-list'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:user_id>/projects/', UserProjects.as_view(), name='user-projects'),
    path('username/<str:username>/', UsernameSearch.as_view(), name='username-search'),
]
