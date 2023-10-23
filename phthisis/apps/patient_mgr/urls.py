from django.urls import path

from apps.patient_mgr.views import test


urlpatterns = [
    path('test/', test.TestAPIView.as_view()),  # 重置密码
]
