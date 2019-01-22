from django.urls import path

from label.views import label

urlpatterns = [
    path('label/', label, name='label'),
]