from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views.user_viewset import UserViewSet
from users.views.report_view import report_view

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('report/', report_view),         # GET /users/report/
    path('', include(router.urls)),       # GET /users/, POST /users/, etc
]
