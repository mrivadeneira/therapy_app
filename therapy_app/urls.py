from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('frontend.urls')),
    path('api/', include('patients.urls')),
    path('api/', include('therapists.urls')),
    path('api/', include('accounting.urls')),
    path('api/', include('security.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]