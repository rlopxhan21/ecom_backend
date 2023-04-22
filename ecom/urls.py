from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # User Account
    path('auth/', include('useraccount.urls')),

    # Products
    path('product/', include("products.urls")),
]
