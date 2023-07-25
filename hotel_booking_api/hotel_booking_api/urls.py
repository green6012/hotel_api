


from django.contrib import admin
from django.urls import path, include
from user_auth.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Các URLs khác của project
    path('api_booking/',include('hotel.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'), # Thêm URL cho API view đăng nhập
    path('user_auth/', include('user_auth.urls')), # Thêm URLs của ứng dụng user_auth vào đây
]
