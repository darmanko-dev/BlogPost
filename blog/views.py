from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required 
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.views.generic import CreateView
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import Http404
# from .mokes import Post

@login_required(login_url="login")
def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts , 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
            posts = paginator.page(1)
    except EmptyPage:
        posts =paginator.page(paginator.num_pages)
    return render(request , "blog/index.html", {'posts' : posts})

@login_required(login_url="login")
def show(request , id):
    post = get_object_or_404(Post , pk = id)
    comments = Comment.objects.filter(post =post).order_by('-id')
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=post ,user=request.user, content=content)
            comment.save()
            return redirect('index')
    else:
        comment_form = CommentForm()
        
    context = {
        'post':post,
        'comment':comments,
        'comment_form':comment_form
    }
   
    return render(request , 'blog/show.html' , context)

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'blog/search_results.html', context)


@login_required(login_url="login")
def AddPost(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        posts = Post.objects.create(
            title = title,
            body = body
        ) 
        posts.save()
        return redirect('index')
        
    return render(request, "blog/add_Post.html" , {"form":form} )


@login_required(login_url="login")
def updatePost(request , id):
    post = get_object_or_404(Post , id = id)
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        post_to_update = Post.objects.filter(pk = post.id)
        post_to_update.update(
            title = title,
            body = body
        )
        return redirect("index")
        
    return render(request , "blog/updatePost.html" , {"post":post})
        

@login_required(login_url="login")
def deletePost(request , id):
    post = get_object_or_404(Post , id = id)
    if request.method == "POST":
        post.delete()
        return redirect('index')

    return render(request , "blog/deletPost.html" , {"post" : post})

def add_comment_to_post(request, id):
    post = get_object_or_404(Post,  id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('show', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.approve()
    return redirect('show', id=comment.post.id)

@login_required
def comment_remove(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect('show', id=comment.post.id)