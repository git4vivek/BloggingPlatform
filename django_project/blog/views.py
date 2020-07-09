from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse ##
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView,CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# posts = [
#     {
#         'author': 'Vivek',
#         'title':'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': '04 July 2016'
#     },
#     {
#         'author': 'Jane',
#         'title':'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': '09 July 2016'
#     }
# ]

def home(request):
    context = {
        'posts' : Post.objects.all() #getting all Post objects
    }
    return render(request,'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #Class Views is looking for <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/users_post.html' #Class Views is looking for <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    fields = ['title', 'content']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request,'blog/about.html', {'title':'About'})