from django.conf.urls import url
from . import views

app_name = 'api'

urlpatterns = [
    url('', views.index, name='index'),
]
