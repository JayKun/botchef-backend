from django.conf.urls import url
from . import views

app_name = 'api'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recipes/(?P<id>[0-9]+)/$', views.increment_rating),
    url(r'^recipes/$', views.get_recipe_list),
]
