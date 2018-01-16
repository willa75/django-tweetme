from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
    TweetCreateView,
    TweetDetailView, 
    TweeDeleteView,
    TweetListView,
    TweetUpdateView
    )

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/')),#/tweet/
    url(r'^search/$', TweetListView.as_view(), name='list'), # /tweet/search
    url(r'^create/$', TweetCreateView.as_view(), name='create'), # /tweet/create/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
    url(r'^(?P<pk>\d+)/edit$', TweetUpdateView.as_view(), name='edit'), # /tweet/1/
    url(r'^(?P<pk>\d+)/delete$', TweeDeleteView.as_view(), name='delete'), # /tweet/1/
]