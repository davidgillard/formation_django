from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^$', views.listing), # "/store" va appeller la methode index dans views.py
    url(r'^(?P<album_id>[0-9]+)/$', views.detail),
]
)