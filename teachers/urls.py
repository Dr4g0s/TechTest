from rest_framework.routers import DefaultRouter
from django.urls import path, include
from teachers import views


router = DefaultRouter()
router.register('teachers', views.TeacherViewset)

app_name = 'teachers'

urlpatterns = [
    path('', include(router.urls))
]