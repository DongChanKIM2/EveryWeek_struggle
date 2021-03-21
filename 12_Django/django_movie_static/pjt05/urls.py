from django.contrib import admin
from django.urls import path, include
# 개발 중 필요한 코드들
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # DEBUG=False 일 때, []
