from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'dealers', views.DealerViewSet, basename='dealers')

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/register/', views.RegisterView.as_view(), name='auth_register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/<int:pk>/', views.UserProfileView.as_view(), name='user-profile'),
    path('', include(router.urls)),
]