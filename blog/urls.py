from django.contrib.auth.models import User
from django.urls import path
from . import views
from .views import MainView, LoginView, LogoutView, UserListView, UserDetailView, PostCreateView, UserView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('blog/login', LoginView.as_view(), name='login'),
    path('blog/logout', LogoutView.as_view(), name='logout'),
    path('blog/users', UserListView.as_view(queryset=User.objects.all().order_by('-username')),
         name='user-list'),
    path('blog/user/<int:pk>', UserDetailView.as_view(), name='user-detail'),
    path('blog/posts/create', PostCreateView.as_view(), name='post-create'),
    path('accounts/profile/', UserView.as_view(), name='user-info')
    ]