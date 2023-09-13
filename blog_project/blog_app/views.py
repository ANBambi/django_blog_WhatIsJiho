from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .models import Post


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request, "board_admin")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# def custom_logout(request):
#     logout(request)
#     return redirect("board_client")


def board_admin(request):
    return render(request, "board_admin.html")


def board_client(request):
    return render(request, "board_client.html")


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "post.html", {"form": form})


def write(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        topic = request.POST["topic"]

        Post.objects.create(
            title=title,
            content=content,
            topic=topic,
            author=request.user,  # 현재 로그인한 사용자를 작성자로 설정
            views=0,  # 조회수 초기값 설정
        )
        # create_at은 현재 시간으로 model에서 설정

        # 일단 작성 완료시 board_client로 이동
        return redirect("board_admin")
    return render(request, "write.html")


# Create your views here.
