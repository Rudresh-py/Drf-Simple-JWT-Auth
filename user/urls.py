# myapp/urls.py

from django.urls import path
from .views import CustomTokenObtainPairView, CustomTokenRefreshView, UserCreateView, LogoutView, UserInfoView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserInfoView.as_view(), name='user_info'),
]