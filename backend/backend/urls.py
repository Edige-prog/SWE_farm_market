from django.contrib import admin
from django.urls import path, include
from api.views import MyTokenObtainPairView, CreateBuyerView, CreateFarmerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/buyer/register/", CreateBuyerView.as_view(), name="buyer-register"),
    path("api/farmer/register/", CreateFarmerView.as_view(), name="farmer-register"),
    path("api/token/", MyTokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
    path('users/', include('users.urls')),
]
