from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from account.views import signIn, signOut, shoppingCart
from book.views import searchBooks
from purchases.views import orders, detailedOrder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signIn, name='landingPage'),
    path('signOut/',signOut,name='signOut'),
    path('searchBooks/',searchBooks,name='searchBooks'),
    path('shoppingCart/',shoppingCart,name='shoppingCart'),
    path('orders/',orders,name='orders'),
    path('orders/<int:id>/',detailedOrder,name='detailedOrder'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)