from django.urls import path
from rest_framework.routers import DefaultRouter
from employeeapi.views import EmployeeView

router=DefaultRouter()
router.register("employees",EmployeeView,basename="employees")

urlpatterns =[
    
]+router.urls