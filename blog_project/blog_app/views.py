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
from bs4 import BeautifulSoup


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request, "board_admin")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def board_admin(request):
    posts = Post.objects.order_by("-views")[:7]
    users = User.objects.filter(username="admin").values("username")

    # db에 저장된 글들 불러오기
    return render(request, "board_admin.html", {"posts": posts, "users": users})


def board_client(request):
    posts = Post.objects.order_by("-views")[:7]

    return render(request, "board_client.html", {"posts": posts})


def post(request, post_id):
    db_post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        # 삭제 요청
        if "delete-button" in request.POST:
            db_post.delete()
            return redirect("board_admin")

    db_post.views += 1
    db_post.save()

    # 이전/다음 게시물 가져옴
    previous_post = Post.objects.filter(id__lt=db_post.id).order_by("-id").first()
    next_post = Post.objects.filter(id__gt=db_post.id).order_by("id").first()

    # 같은 주제인 게시물들 중 최신 글 가져옴
    recommended_posts = (
        Post.objects.filter(topic=db_post.topic).exclude(id=db_post.id).order_by("-create_at")[:2]
    )
    # 게시물 내용에서 첫번째 이미지(썸네일) 태그 추출
    for recommended_post in recommended_posts:
        # 이미지 경로 검사
        recommended_post.check_url()
        soup = BeautifulSoup(recommended_post.content, "html.parser")
        image_tag = soup.find("img")
        recommended_post.image_tag = str(image_tag) if image_tag else ""

    # 이미지 경로 검사
    db_post.check_url()
    if previous_post:
        previous_post.check_url()
    if next_post:
        next_post.check_url()

    context = {
        "post": db_post,
        "previous_post": previous_post,
        "next_post": next_post,
        "recommended_posts": recommended_posts,
        "MEDIA_URL": settings.MEDIA_URL,
    }

    return render(request, "post.html", context)


# 될지 안될지 모르는 view_post 부분
# def view_post(request, post_id):
#     article = get_object_or_404(Post, pk=post_id)
#     # 해당 게시물의 방문 횟수누적증가
#     article.increment_visit_count()

#     context = {
#         "post": post,
#     }
#     return render(request, "post.html", context)


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
