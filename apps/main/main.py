from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from common.views import ViewMixin
from .models import Demo
from .serializers import DemoSerializer

param_age = openapi.Parameter(
    'age',
    openapi.IN_QUERY,
    description='user age',
    type=openapi.TYPE_INTEGER
)


class DemoView(generics.CreateAPIView, ViewMixin):

    serializer_class = DemoSerializer

    @swagger_auto_schema(manual_parameters=[param_age])
    def post(self, request, user_id):
        d = Demo(user_id=user_id)
        d.save()
        return self.build_ok_response(data=DemoSerializer(d).data)
