
from django.contrib import admin
from django.urls import path, include
from products import views
from tienda_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('products/', views.products, name='products'),
    #path('home/products/', views.products, name='products'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
