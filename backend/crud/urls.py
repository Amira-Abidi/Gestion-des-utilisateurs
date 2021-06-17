from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
from crud.restapi import views
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token 


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
   
]

  
