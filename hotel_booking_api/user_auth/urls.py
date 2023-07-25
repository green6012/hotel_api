
from django.urls import path
from user_auth.views import UserRegistrationView, UserLoginView, CustomTokenRefreshView, LogoutView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token-refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
