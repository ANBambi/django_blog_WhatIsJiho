from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .models import Post
from django.http import JsonResponse
from django.conf import settings
from django.views import View
from django.core.files.storage import default_storage
from django.contrib.auth.models import User


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
    # top_posts = Post.objects.order_by("-views")[:6]
    # context = {
    #     "top_posts": top_posts,
    # }
    # return render(request, "board_admin.html", context)
    #   이런식으로 조회수 높은 여섯개 가져오기 (?)

    posts = Post.objects.all()
    users = User.objects.filter(username='admin').values('username')
    
    # db에 저장된 글들 불러오기
    return render(request, "board_admin.html", {"posts": posts, "users": users})


def board_client(request):
    # top_posts = Post.objects.order_by("-views")[:6]
    # context = {
    #     "top_posts": top_posts,
    # }
    # return render(request, "board_admin.html", context)
    #   이런식으로 조회수 높은 여섯개 가져오기 (?)
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


# 될지 안될지 모르는 view_post 부분
def view_post(request, post_id):
    article = get_object_or_404(Post, pk=post_id)
    # 해당 게시물의 방문 횟수누적증가
    article.increment_visit_count()

    context = {
        "post": post,
    }
    return render(request, "post.html", context)


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

# 이미지 업로드
class image_upload(View):
    # 사용자가 이미지 업로드 하는경우 실행
    def post(self, request):
        # file필드 사용해 요청에서 업로드한 파일 가져옴
        file = request.FILES["file"]

        # 저장 경로 생성
        filepath = "uploads/" + file.name

        # 파일 저장
        filename = default_storage.save(filepath, file)

        # 파일 URL 생성
        file_url = settings.MEDIA_URL + filename

        # 이미지 업로드 완료시 JSON 응답으로 이미지 파일의 url 반환
        return JsonResponse({"location": file_url})