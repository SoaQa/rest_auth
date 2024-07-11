from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [

]

urlpatterns += router.urls
