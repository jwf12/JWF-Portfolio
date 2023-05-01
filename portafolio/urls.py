from django.urls import path
from .views import ListProjects

app_name='api'
urlpatterns = [
    path('', ListProjects.as_view(), name='get')
]