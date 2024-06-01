from django.urls import path

from api.views import Test

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('test', Test.as_view()),
]
