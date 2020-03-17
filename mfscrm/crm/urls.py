from django.conf.urls import url
from . import views
from django.urls import path, re_path, reverse_lazy
from templates import registration
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView
from .views import  SignUpView


app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('service_list', views.service_list, name='service_list'),
    path('service/create/', views.service_new, name='service_new'),
    path('service/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('service/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('product_list', views.product_list, name='product_list'),
    path('product/create/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('customer/<int:pk>/summary/', views.summary, name='summary'),
    #path('password-reset', PasswordResetView.as_view(template_name='registration/forgot_password.html'), name='password-reset'),
    #url(r'^password/$', views.change_password, name='password_change_form'),
    path('password_change', PasswordChangeView.as_view(template_name = 'registration/password_change_form.html'), name='password-change-form'),
    path('password_change_done', PasswordChangeDoneView.as_view(template_name = 'registration/password_change_done.html'), name='password-change-done'),
    path('password_reset', PasswordResetView.as_view(template_name='registration/forgot_password.html'), name='password-reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password-reset-done'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password-reset-confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password-reset-complete'),
    path('signup/', SignUpView.as_view(), name='signup')
]
