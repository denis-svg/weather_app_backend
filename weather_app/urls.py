from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/user/register", CreateUserView.as_view(), name="register"),
    path("api/v1/token", token_obtain_pair, name="get token"),
    path("api/v1/token/refresh", token_refresh, name="refresh token"),
    path('api-auth/', include('rest_framework.urls'))
]
