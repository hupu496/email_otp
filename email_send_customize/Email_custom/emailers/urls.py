from django.urls import path
from . import views

urlpatterns = [
    path('', EmailAttachementView.as_view(), name='emailattachment')
]