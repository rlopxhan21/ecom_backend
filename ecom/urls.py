from django.contrib import admin
from django.urls import path, include

from django.conf import settings  # new
from django.conf.urls.static import static  # new

urlpatterns = [
    path('admin/', admin.site.urls),

    # User Account
    path('auth/', include('useraccount.urls')),

    # Products
    path('product/', include("products.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
