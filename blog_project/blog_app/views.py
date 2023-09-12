from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    if request.method == "POST":
        form == AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return render(request, "login.html")
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
        if form.is_Valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "post.html", {"form": form})


def write(request):
    return render(request, "write.html")


# Create your views here.
