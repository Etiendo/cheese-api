from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def ping(request):
    return HttpResponse("pong")


handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'

urlpatterns = [
    url(r'ping', ping),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(
        r'^',
        include("app_backend.users.urls", namespace="users")
    ),
    url(
        r'^',
        include("app_backend.shops.urls", namespace="shops")
    ),

]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
