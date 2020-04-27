from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from account.views import signIn, signOut
from book.views import searchBooks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signIn, name='landingPage'),
    path('signOut',signOut,name='signOut'),
    path('searchBooks',searchBooks,name='searchBooks')
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)