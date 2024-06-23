from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class ShowNewsView(ListView):
    model = News
    template_name = 'myApp/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Main page'
        return ctx


class UserAllNewsView(ListView):
    model = News
    template_name = 'myApp/user_news.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(author=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)

        ctx['title'] = f"Articles from {self.kwargs.get('username')}"
        return ctx


class NewsDetailView(DetailView):
    model = News
    template_name = 'myApp/news_detail.html'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


class CreateNewsVeiw(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'myApp/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsVeiw, self).get_context_data(**kwards)

        ctx['title'] = 'Adding article'
        ctx['btn_text'] = 'Add article'
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateNewsVeiw(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'myApp/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsVeiw, self).get_context_data(**kwards)

        ctx['title'] = 'Update article'
        ctx['btn_text'] = 'Update'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'myApp/delete-news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False


def contacts(request):
    return render(request, 'myApp/contacts.html', {'title': 'Contacts page'})