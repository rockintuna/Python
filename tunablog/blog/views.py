from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from blog.models import Post
from django.contrib.auth import get_user_model

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)

def post_add(request):
    if request.method == 'POST':
        User = get_user_model()
        title = request.POST['title']
        content = request.POST['content']
        author = User.objects.get(username='jilee')
        post = Post.objects.create(
            author=author,
            title=title,
            content=content,
        )
        post.publish()
        post_pk = post.pk
        return redirect(post_detail, pk=post_pk)

    elif request.method == 'GET':
        return render(request, 'blog/post_add.html')

def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return render(request, 'blog/post_delete.html')

    elif request.method =='GET':
        return HttpResponse('잘못된 접근입니다.')