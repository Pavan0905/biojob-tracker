from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_job, name='submit'),
    path('update/<int:job_id>/<str:status>/', views.update_status, name='update_status'),
]