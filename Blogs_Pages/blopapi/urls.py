from django.urls import path
from blopapi.views import BlogApiView

urlpatterns = [
    path('blog/',BlogApiView.as_view())

]