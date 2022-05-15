from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View, generic
from django.views.generic import CreateView, ListView

from blog.forms import PostForm
from blog.models import Post


class MainView(View):
    def get(self, request):
        return render(request, 'blog/main.html')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'


class UserView(View):
    def get(self, request):
        return render(request, 'blog/user_info.html')


class UserLogoutView(LogoutView):
    template_name = 'blog/logout.html'


class UserListView(generic.ListView):
    model = User
    template_name = 'blog/user_list.html'
    context_object_name = 'user_list'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'blog/user_detail.html'
    context_object_name = 'user_detail'

class PostCreateView(View):
    def get(self, request):
        post_form = PostForm
        return render(request, 'blog/post_form.html', {'post_form': post_form})


    def post(self, request):
        post_form = PostForm(request.POST)
        post_form.author = request.user
        new_post = post_form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        return HttpResponseRedirect(reverse('user-detail', args=[request.user.id]))



    # def post(self, request):
    #     post_form = PostForm(request.POST)
    #     if post_form.is_valid():
    #         new_post = post_form.save(commit=False)
    #         new_post.author = request.user
    #         new_post.save()
    #     return HttpResponseRedirect(reverse('user-detail', args=[request.user.id]))



# class PostCreateView(View):
#
#     def get(self, request):
#         profile_id = request.user.id
#         post_form = PostForm()
#         return render(request, 'blog/post_create.html', context={'post_form': post_form})
#
#     def post(self, request):
#
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#
#
#         return render(request, 'blog/post_create.html', context={'post_form': post_form})
