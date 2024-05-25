from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView
from .models import Post

# Create your views here.
class BlogListView(ListView): 
    model = Post
    template_name ="home.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "new_post.html"
    fields = ["title", "author", "body"]

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_details.html"
    fields = ["title", "body"]

class BlogUpdateView(UpdateView):
     model = Post
     template_name = "update.html"
     fields = ["title", "body"]