from django.urls import path
from .views import FormMatcherView

urlpatterns = [
    path('get_form', FormMatcherView.as_view(), name='get_form'),
]