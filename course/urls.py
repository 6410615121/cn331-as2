from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<str:courseID>', views.course_detail, name='course_detail'),
    path('<str:courseID>/request_quota/', views.quota_request, name='request_quota'),
    path('quota_status/', views.quota_status, name="quota_status"),
    path('course/quota_withdraw/<str:courseID>/', views.quota_withdraw, name="quota_withdraw"),
]
