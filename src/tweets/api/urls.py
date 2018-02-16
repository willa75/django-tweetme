from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
	TweetCreateAPIView,
    TweetListAPIView
    )

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'), # /api/tweet/
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), # /api/tweet/create/
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
    # url(r'^(?P<pk>\d+)/edit$', TweetUpdateView.as_view(), name='edit'), # /tweet/1/
    # url(r'^(?P<pk>\d+)/delete$', TweeDeleteView.as_view(), name='delete'), # /tweet/1/
]