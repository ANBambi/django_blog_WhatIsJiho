from django.shortcuts import render


def login(request):
    return render(request, "login.html")


def board_admin(request):
    return render(request, "board_admin.html")


def board_client(request):
    return render(request, "board_client.html")


def board(request):
    return render(request, "board.html")


def write(request):
    return render(request, "write.html")


# Create your views here.
