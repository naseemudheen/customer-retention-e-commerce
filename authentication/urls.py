
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(('user.urls'))),
    path('api/', include(('api.urls'))),
    path('', include(('client.urls'))),
    path('dashboard/', include(('dashboard.urls'))),


    # path('', include('pwa.urls')),

]