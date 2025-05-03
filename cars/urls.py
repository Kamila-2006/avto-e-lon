from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'cars', views.CarViewSet, basename='cars')

urlpatterns = [
    path('makes/', views.MakeListCreateView.as_view(), name='makes'),
    path('models/', views.ModelListCreateView.as_view(), name='models'),
    path('make/<int:make_id>/models/', views.ModelsByMake.as_view(), name='models-by-make'),
    path('body_type/', views.BodyTypeListCreateView.as_view(), name='body-type'),
    path('features/', views.FeatureListCreateView.as_view(), name='feature'),
    path('', include(router.urls))
]