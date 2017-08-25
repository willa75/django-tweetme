from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet
# Create your views here.

class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()
	template_name = "tweets/detail_view.html"

	def get_object(self):
		pk = self.kwargs.get("pk")
		return Tweet.objects.get(id=pk)

class TweetListView(ListView):
	queryset = Tweet.objects.all()
	template_name = "tweets/list_view.html"


def tweet_detail_view(request, id=1):
	obj = Tweet.objects.get(id=id)
	print(obj)
	context = {
		"object": obj
	}
	return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request, id=1):
	queryset = Tweet.objects.all()
	print(queryset)
	for obj in queryset:
		print(obj.content)
	context = {
		"object_list": queryset
	}
	return render(request, "tweets/list_view.html", context)