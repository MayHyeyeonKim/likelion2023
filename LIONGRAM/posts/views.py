from wsgiref.util import request_uri
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from .forms import PostBaseForm, PostCreateForm, PostDetailForm
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_at') #Post 전체 조회 / 최신순으로 정렬 order_by('-created_at')
    context = {
            "post_list" : post_list
        }
    return render(request, 'index.html', context)

def post_list_view(request):
    # post_list = Post.objects.all() #Post 전체 조회
    post_list = Post.objects.filter(writer=request.user) #Post.writer가 현재 로그인인 것 조회
    context = {
        "post_list" : post_list
    }
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect('index')
    context = {
        'post' : post,
        'form' : PostDetailForm(),
    }
    return render(request, 'posts/post_detail.html', context)

@login_required # 이 함수는 로그인했을때만 처리한다
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content,
            writer=request.user,
        )
        return redirect('index') 

def post_create_form_view(request):
    if request.method == 'GET':
        form = PostCreateForm()
        context = {'form': form}
        return render(request, 'posts/post_form2.html', context)
    else:
        form = PostCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                writer=request.user
            )
        else:
            return redirect('posts:post-create')
        return redirect('index')

def post_update_view(request,id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    if request.method == 'GET':
        context = { 'post':post }
        return render(request, 'posts/post_form.html', context)
    elif request.method == 'POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        print(new_image)
        print(content)

        if new_image:
            post.image.delete()
            post.image = new_image

        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)

def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.writer:
        return Http404('잘못된 접근입니다다다!!')
    
    if request.method == "GET":
        context = { 'post' : post }
        # print(post.id)
        return render(request, 'posts/post_confirm_delete.html', context)
    else:
        post.delete()
        return redirect('index')

def url_view(request):
    print('url_view()') #브라우저에서 새로고침해보면 터미널에 찍힌다.
    data = {'code':'001', 'msg':'ok'}
    # return HttpResponse('url_view')
    return JsonResponse(data)

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    # print(username)
    # print(request.GET)
    return HttpResponse(username)

def funtion_view(request):
    print(f'request.method: {request.method}')
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'
    ordering = ['-id']