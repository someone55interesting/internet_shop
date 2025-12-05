from django.contrib import admin
from django.urls import path, include # <-- Убедись, что include импортирован!
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Корзина и Заказы
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    
    # --- ВОТ ЭТОЙ ЧАСТИ НЕ ХВАТАЕТ ---
    # Это подключает готовые URL для входа и выхода (login, logout)
    path('accounts/', include('django.contrib.auth.urls')), 
    # ---------------------------------

    # Магазин (должен быть в конце)
    path('', include('shop.urls', namespace='shop')),
]

# Для картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)