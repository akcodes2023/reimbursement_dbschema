from django.urls import path, include
from . import views

# For TokenAuthentication
from rest_framework.authtoken.views import obtain_auth_token

"""
# from .views import EmployeeViewSet

# import routers
# from rest_framework import routers
# from rest_framework.routers import DefaultRouter

# define the router
# router = routers.DefaultRouter()

# router = DefaultRouter()

# define the router path and viewset to be used
# router.register(r'geeks', GeeksViewSet)
# router.register(r'employees', EmployeeViewSet)
"""

urlpatterns = [
    path('',views.homepage, name=""),
    # path('api-auth/', include('rest_framework.urls')),
    path('register/',views.register, name="register"),
    path('my-login/',views.my_login, name="my-login"),
    path('dashboard/',views.dashboard, name="dashboard"),
    # path('', include(router.urls)),
    path('api/employees/', views.employee_list, name='employee-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
