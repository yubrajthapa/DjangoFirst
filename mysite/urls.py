from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
# for displaying image import settings and static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('users/', include('users.urls')),
 
]

# displaying an image
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
