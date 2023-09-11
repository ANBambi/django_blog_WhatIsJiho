from django.urls import path
from . import views


urlpatterns = [
    # 나머지 URL 패턴들을 추가
    path("", views.login, name="login"),
    # path('logout/', views.logout, name='logout'),
    path("board_admin", views.board_admin, name="board_admin"),
    path("board_client", views.board_client, name="board_client"),
    path("board", views.board, name="board"),
    path("write", views.write, name="write"),
]
