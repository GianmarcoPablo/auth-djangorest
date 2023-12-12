from django.urls import path, include
from rest_framework import routers
from tareas import views

#router = routers.DefaultRouter()
#router.register("tareas", views.TaskViewSet, "tareas")

urlpatterns = [
    #path("api/v1/", include(router.urls)),
    path("api/v1/login/", views.login),
    path("api/v1/signup/", views.signup),
    path("api/v1/test-token/", views.test_token),
]
