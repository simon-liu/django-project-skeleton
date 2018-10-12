from django.conf.urls import url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.main.urls import urlpatterns as main_urlpatterns

schema_view = get_schema_view(
    openapi.Info(
        title="Nester API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    url(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(),
        name='schema-json'
    ),
    url(
        r'^swagger/$',
        schema_view.with_ui('swagger'),
        name='schema-swagger-ui'
    ),
]

urlpatterns += main_urlpatterns
