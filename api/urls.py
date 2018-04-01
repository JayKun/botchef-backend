from django.conf.urls import url
from . import views

app_name = 'api'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recipes/vote/(?P<id>[0-9]+)/$', views.increment_rating),
    url(r'^recipes/$', views.get_recipe_list),
    url(r'^recipes/(?P<id>[0-9]+)/$', views.get_recipe_details),
    url(r'^user/$', views.create_user),
]
