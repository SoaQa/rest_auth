from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('auth', views.AuthViewSet, basename='auth')

urlpatterns = [

]

urlpatterns += router.urls
