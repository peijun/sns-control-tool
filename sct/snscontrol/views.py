from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.

def index(request):
    return HttpResponse("Hello")

@login_required
def home(request):
    return render(request, 'snscontrol/home.html')

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            print(request)
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.image1 = request.FILES.get('image1', None)
            post.image2 = request.FILES.get('image2', None)
            post.image3 = request.FILES.get('image3', None)
            post.image4 = request.FILES.get('image4', None)
            post.save()
    else:
        form = PostForm()
    return render(request, 'snscontrol/add_post.html', {'form': form})

@login_required
def view_post(request):
    posts = Post.objects.all()
    return render(request, 'snscontrol/view_post.html', {'posts': posts})

@login_required
def master_post(request):
    posts = Post.objects.all()
    return render(request, 'snscontrol/master_post.html', {'posts': posts})

@login_required
def approve_post(request,pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    if user.authority <= 1:
        if request.method == 'POST':
            post.is_approval = True
            post.save()
        return redirect('master_post')
    else:
        return HttpResponse("Sorry, you CANT this action")