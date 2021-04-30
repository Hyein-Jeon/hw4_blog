from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:post_id>', more, name="more"),
    path('make/', make, name="make"),
    path('generate/', generate, name="generate"),
    path('change/<str:id>', change, name="change"),
    path('renew/<str:id>', renew, name="renew"),
    path('remove/<str:id>', remove, name="remove"),
]
