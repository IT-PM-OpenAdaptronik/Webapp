from django.urls import path

from apps.process import views

app_name = 'process'
urlpatterns = [
    path('', views.fromDashboard, name='fromDashboard'),
    path('analysis/', views.analysis, name='analysis')
]