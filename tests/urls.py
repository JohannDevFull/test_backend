from drf_spectacular.views import SpectacularRedocView
from django.urls import path

urlpatterns = [
    path( 'tests/' , SpectacularRedocView.as_view( url_name='tests' ) , name='tests' ),
]
