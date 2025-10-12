from django.urls import path
from .views import test_r2_upload

urlpatterns = [
    path("test-r2/", test_r2_upload, name="test_r2_upload"),
]
