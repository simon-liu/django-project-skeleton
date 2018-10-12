from django.urls import path

from .main import DemoView

urlpatterns = [
    path('<int:user_id>/demo',
         DemoView.as_view()),
]
