from django.urls import path

from slider.views import MainPageView

urlpatterns = [
    path("", MainPageView.as_view(), ),
]
