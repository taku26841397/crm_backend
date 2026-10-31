from django.urls import path
from .views import CustomerListAPI,CustomerDetailAPI,CustomerUpdateAPI,CustomerDeleteAPI,DashbordAPIView,ActivityListAPI,ActivityListCreateAPI,ActivityUpdateAPI,ActivityDetailAPI,ActivityDeleteAPI,UserAPI,ProfileAPI

urlpatterns = [
    path('dashboard/',DashbordAPIView.as_view()),
    path('customers/',CustomerListAPI.as_view()),
    path('custmers/new/',CustomerListAPI.as_view()),
    path('customers/<int:pk>/',CustomerDetailAPI.as_view()),
    path('customers/<int:pk>/edit/',CustomerUpdateAPI.as_view()),
    path('customers/<int:pk>/delete/',CustomerDeleteAPI.as_view()),
    
    path('activities/',ActivityListAPI.as_view()),
    path('customers/<int:pk>/activities/',ActivityListCreateAPI.as_view()),
    path('activities/<int:activity_id>/',ActivityDetailAPI.as_view()),
    path('customers/<int:pk>/activities/<int:activity_id>/edit/',ActivityUpdateAPI.as_view()),
    path('activities/<int:activity_id>/delete/',ActivityDeleteAPI.as_view()),
    
    path('me/',UserAPI.as_view()),
    path('profile/',ProfileAPI.as_view()),
    path('profile/<int:pk>',ProfileAPI.as_view()),
    
    
]
