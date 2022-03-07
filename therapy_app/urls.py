from django.contrib import admin
from django.urls import path, include
#from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include('patients.urls')),
    path('api/', include('therapists.urls')),
    path('api/', include('accounting.urls')),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]