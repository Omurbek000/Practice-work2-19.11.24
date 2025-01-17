from django.shortcuts import render, redirect
from .forms import Form
from .models import Request


def create_request(request):
    if request.method == "POST":
        form = Request.Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_request.html")

    else:
        form = Form
    return render(request, "requests/create_request.html", {"form": form})


def request_list(request):
    requests = Request.objects.all()
    return render(request, "requests/request_list.html", {"requests": requests})
