from django.shortcuts import render

from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    form = PostForm()
    # print (request.POST)

    # if(request.POST):
    # 	print("in post request")

    # if(request.GET):
    # 	print("in GET request")
    return render(request, 'home.html', {'form': form})

@login_required
def vote_candidate(request):
    form = PostForm()
    return render(request, 'voting_form.html', {'form': form})


@login_required
def vote(request):
    if(request.POST):
        print("in post request")
    return render(request, 'voting_home.html')


@login_required
def thanks(request):
    return render(request, 'thanks.html')

@login_required
def new_user(request):
    return render(request, 'post_edit.html')


