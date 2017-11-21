from django.conf.urls import url

from .views import (
    TweetCreateView,
    TweetDetailView, 
    TweeDeleteView,
    TweetListView,
    TweetUpdateView
    )

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='list'), # /tweet/
    url(r'^create/$', TweetCreateView.as_view(), name='create'), # /tweet/create/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
    url(r'^(?P<pk>\d+)/edit$', TweetUpdateView.as_view(), name='edit'), # /tweet/1/
    url(r'^(?P<pk>\d+)/delete$', TweeDeleteView.as_view(), name='delete'), # /tweet/1/
]