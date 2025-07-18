from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, trade_here_view 
from core import views 

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('trade/', views.trade_here_view, name='trade_here'), 
    path('trade/submit/', views.trade_here_view, name='trade_here_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
