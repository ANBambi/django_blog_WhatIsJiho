from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # 나머지 URL 패턴들을 추가
    path("", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("board_admin", views.board_admin, name="board_admin"),
    path("board_client", views.board_client, name="board_client"),
    path("post", views.post, name="post"),
    path("write", views.write, name="write"),
]
