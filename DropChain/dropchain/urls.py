from django.conf.urls import url
from dropchain import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join_ch/$', views.join_ch),
    #url(r'^snippets/$', views.snippet_list),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
