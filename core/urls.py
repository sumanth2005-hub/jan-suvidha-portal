from django.urls import path
from . import views

urlpatterns = [
    # Landing & citizen pages
    path('', views.landing, name='landing'),
    path('register/', views.register, name='register'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('results/', views.results, name='results'),
    path('documents/<str:scheme_id>/', views.documents, name='documents'),

    # API endpoints
    path('api/switch-language/', views.api_switch_language, name='api_switch_language'),
    path('api/register/', views.api_register, name='api_register'),
    path('api/send-otp/', views.api_send_otp, name='api_send_otp'),
    path('api/verify-otp/', views.api_verify_otp, name='api_verify_otp'),
    path('api/check-eligibility/', views.api_check_eligibility, name='api_check_eligibility'),
    path('api/upload-document/', views.api_upload_document, name='api_upload_document'),
    path('api/locations/', views.api_locations, name='api_locations'),
    path('api/ask-question/', views.api_ask_question, name='api_ask_question'),
    path('api/schemes/', views.api_schemes, name='api_schemes'),

    # Admin
    path('admin-portal/login/', views.admin_login, name='admin_login'),
    path('admin-portal/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-portal/logout/', views.admin_logout, name='admin_logout'),
    path('api/admin/analytics/', views.api_admin_analytics, name='api_admin_analytics'),
    path('api/admin/send-reminder/', views.api_send_reminder, name='api_send_reminder'),
    path('api/admin/sms-logs/', views.api_sms_logs, name='api_sms_logs'),
]
