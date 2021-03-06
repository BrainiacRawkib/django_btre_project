from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
    path('listings/', include('listings.urls', namespace='listings')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

