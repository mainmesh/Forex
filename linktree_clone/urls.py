from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import home
from core import views 

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('trade-here/', views.trade_here, name='trade_here'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
