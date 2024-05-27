from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("products/", include("products.urls")),
    path("bag/", include("bag.urls")),
    path("checkout/", include("checkout.urls")),
    path("profile/", include("profiles.urls")),
    path("contact/", include("contact.urls")),
    path("faq/", include("faq.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = "vintage.views.error_400"
handler403 = "vintage.views.error_403"
handler404 = "vintage.views.error_404"
handler500 = "vintage.views.error_500"
