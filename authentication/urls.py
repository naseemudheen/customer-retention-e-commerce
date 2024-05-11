
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('user.urls'))),
    path('api/', include(('api.urls'))),

    # path('', include('pwa.urls')),

]