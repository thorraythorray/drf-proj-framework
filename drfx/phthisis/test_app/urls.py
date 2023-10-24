from django.urls import path

from drfx.phthisis.test_app import views


urlpatterns = [
    path('test/', views.TestAPIView.as_view()),
]
