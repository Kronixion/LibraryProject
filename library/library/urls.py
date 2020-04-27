from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from account.views import signIn, signOut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signIn, name='signIn'),
    path('signOut',signOut,name='signOut')
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)