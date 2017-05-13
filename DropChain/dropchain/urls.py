from django.conf.urls import url
from dropchain import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^prova/$', views.prova),

    url(r'^new_user/$', views.NewUser),
    url(r'^new_proj/$', views.NewProject),
    url(r'^new_t_ch/$', views.NewTypeChallenge),

    url(r'^view_profile/$', views.view_profile),
    url(r'^view_proj/$', views.view_proj),
    url(r'^view_t_ch/$', views.view_t_ch),

    url(r'^load_t_ch/$', views.load_t_ch),
    url(r'^load_proj/$', views.load_proj),

    url(r'^join_ch/$', views.join_ch),

    #url(r'^snippets/$', views.snippet_list),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
