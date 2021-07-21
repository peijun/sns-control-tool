from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from .twitter import TwitterUtil, TwitterUpload

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
            post.approver = user
            post.save()
        return redirect('master_post')
    else:
        return HttpResponse("Sorry, you CANT this action")

@login_required
def publish_twitter(request,pk):
    post = get_object_or_404(Post,pk=pk)
    
    if post.is_publish_twitter == True:
        return HttpResponse("This post was published")
    else:
        #try:
            if request.method == 'POST':
                t = TwitterUtil()
                t_up = TwitterUpload()

                if post.image1:
                    with open(post.image1.path, "rb") as imagefile:
                        imagedata1 = imagefile.read()
                    id_img1 = t_up.upload_media(imagedata1)
                    
                    if post.image2:
                        with open(post.image2.path, "rb") as imagefile:
                            imagedata2 = imagefile.read()
                        id_img2 = t_up.upload_media(imagedata2)

                        if post.image3:
                            with open(post.image3.path, "rb") as imagefile:
                                imagedata3 = imagefile.read()
                            id_img3 = t_up.upload_media(imagedata3)

                            if post.image4:
                                with open(post.image4.path, "rb") as imagefile:
                                    imagedata4 = imagefile.read()
                                id_img4 = t_up.upload_media(imagedata4)

                                t.post_with_media(text=post.content,media_ids=",".join([id_img1, id_img2, id_img3, id_img4]))
                            else:
                                t.post_with_media(text=post.content,media_ids=",".join([id_img1, id_img2, id_img3]))
                        else:
                            t.post_with_media(text=post.content,media_ids=",".join([id_img1, id_img2]))
                    else:
                        t.post_with_media(text=post.content,media_ids=",".join([id_img1]))
                else:
                    t.post(text=post.content)

                post.is_publish_twitter = True
                post.is_public = True
                post.save()

                return redirect('finish_post')
        #except:
            #return HttpResponse("Sorry, something went wrong")

@login_required
def finish_post(request):
    return render(request,'snscontrol/complete.html')
        