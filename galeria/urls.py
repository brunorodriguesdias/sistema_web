from django.urls import URLPattern, path
from galeria.views import index

urlpatterns = [
    path('', index)
]