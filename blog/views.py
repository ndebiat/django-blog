from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


def home(request):
    # create a list of posts (content stored in dictionaries) by passing the dictionaries into a list
    context = {
        'posts': Post.objects.all()  # Post.objects.all() used to create a list of all the posts in the db
    }

    # to render an html page, first pass a request, the pass the html pag path, and optionally any data
    # you'd like to use in the html page - in this case, you'd like to incorporate post data into the home.html page
    return render(request, 'blog/home.html', context)


# class based view for viewing the blog list
class PostListView(ListView):
    model = Post
    # set the template name
    # by default, django looks for a template with the following naming convention
    # <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # change the ordering from newest to oldest
    ordering = ['-date_posted']
    # set up class based pagination to allow the posts to be split by pages
    # this means 5 posts per page
    paginate_by = 5  # need to set up html to set up buttons that move between pages


# class based view for viewing the author list
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    # set up function to get specific user
    def get_queryset(self):
        # if user doesn't exist, get 404
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# used to display each individual blog post
class PostDetailView(DetailView):
    model = Post
    # default template name (post_detail) is used


# used to display form to create a post
# use a login mixin (can't use decorators on classes) to require user to be logged in
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # set form fields
    fields = ['title', 'content']

    # method to set the author of the post
    def form_valid(self, form):
        # tells the form to set user as author
        form.instance.author = self.request.user
        return super().form_valid(form)


# used to update form
# use a pass test mixin to allow users only to edit own post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # set form fields
    fields = ['title', 'content']

    # method to set the author of the post
    def form_valid(self, form):
        # tells the form to set user as author
        form.instance.author = self.request.user
        return super().form_valid(form)

    # test to ensure that user only edits own posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# used to delete blog post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    # test to ensure that user only deletes own posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    title = {
        'title': 'About'
    }

    return render(request, 'blog/about.html', title)
