from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from oscar.app import application, shop
from paypal.express.dashboard.app import application

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'', include(application.urls)),
    (r'^checkout/paypal/', include('paypal.express.urls')),
    # Optional
    (r'^dashboard/paypal/express/', include(application.urls)),
    (r'', include(shop.urls)),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
