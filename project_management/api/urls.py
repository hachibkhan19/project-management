from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register('users/register', UserViewSet)
router.register('projects', ProjectViewSet)
router.register('project-members', ProjectMemberViewSet)
router.register(r'projects/(?P<project_id>\d+)/tasks', TaskViewSet, basename='project-tasks')
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'tasks/(?P<task_id>\d+)/comments', CommentViewSet, basename='task-comments')
router.register(r'comments', CommentViewSet, basename="comments")


urlpatterns = [
    path('', include(router.urls)),
    path('users/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),

]

