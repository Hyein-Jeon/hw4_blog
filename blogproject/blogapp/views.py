from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts':posts})

def more(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'more.html', {'post':post})

def make(request):
    return render(request, 'make.html')

def generate(request):
    make_post = Post()
    make_post.post_title = request.POST['title']
    make_post.post_writer = request.POST['writer']
    make_post.post_body = request.POST['body']
    make_post.post_date = timezone.now()
    make_post.save()
    return redirect('more', make_post.id)

def change(request, id):
    change_post = Post.objects.get(id = id)
    return render(request, 'change.html', {'post':change_post})


def renew(request, id):
    renew_post = Post.objects.get(id = id)
    renew_post.post_title = request.POST['title']
    renew_post.post_writer = request.POST['writer']
    renew_post.post_body = request.POST['body']
    renew_post.post_date = timezone.now()
    renew_post.save()
    return redirect('more', renew_post.id)

def remove(request, id):
    remove_blog = Post.objects.get(id = id)
    remove_blog.delete()
    return redirect('main')