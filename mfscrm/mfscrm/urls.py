from django.contrib import admin, auth
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('home/', TemplateView.as_view(template_name='crm/home.html'), name='home'),
    path('', include('django.contrib.auth.urls')),

    # path('accounts/', include('django.contrib.auth.urls')),
    # path('users/', include('django.contrib.auth.urls')),
]
