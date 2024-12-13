from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from store.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('payment/', include('payment.urls')),
    path('health/', health_check, name='health_check'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
