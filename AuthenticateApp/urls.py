from django.urls import path, include
from . import views
from .views import EmployeeViewSet

# import routers
# from rest_framework import routers
from rest_framework.routers import DefaultRouter

# define the router
# router = routers.DefaultRouter()
router = DefaultRouter()

# define the router path and viewset to be used
# router.register(r'geeks', GeeksViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('',views.homepage, name=""),
    path('register/',views.register, name="register"),
    path('my-login/',views.my_login, name="my-login"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))

]
