from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 나머지 URL 패턴들을 추가
    path("", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="board_client"), name="logout"),
    # path("board_admin", views.board_admin, name="board_admin"),
    path("board_client", views.board_client, name="board_client"),
    path("post/<int:post_id>/", views.post, name="post"),
    path("write", views.write, name="write"),
    path("edit_post/<int:post_id>/", views.edit_post, name="edit_post"),
    path("image-upload/", views.image_upload.as_view(), name="image_upload"),
    path("post/<str:topic>/", views.board_client, name="post_list_by_topic"),
    path("autocomplete/", views.autocomplete, name="autocomplete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
