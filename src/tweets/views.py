from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, 
    ListView, 
    CreateView, 
    UpdateView,
    DeleteView
)

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet

# Create your views here.

class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    success_url = "/tweet/create/"
    login_url = '/admin/'

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    success_url = "/tweet/"

class TweeDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    queryset = Tweet.objects.all()
    model = Tweet
    success_url = reverse_lazy("home")
    template_name = "tweets/delete_confirm.html"

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"

    def get_object(self):
        pk = self.kwargs.get("pk")
        return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = "tweets/list_view.html"
