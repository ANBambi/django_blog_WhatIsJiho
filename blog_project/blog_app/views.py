from django.shortcuts import render, redirect
from .forms import PostForm


def login(request):
    return render(request, "login.html")


def board_admin(request):
    return render(request, "board_admin.html")


def board_client(request):
    return render(request, "board_client.html")


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_Valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "post.html", {"form": form})


def write(request):
    return render(request, "write.html")


# Create your views here.
