from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from skflite import settings
from .forms import UserPostForm, NewsForm, EventForm
from .models import UserPost, News, Event


@login_required
def user_post(request):
    if request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserPostForm()
    return render(request, "home.html", {
        'form': form
    })

def delete_post(request, pk):
    post = get_object_or_404(UserPost, pk=pk)
    post.delete()
    return redirect('/')


@login_required
def news(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/social/News')
        else:
            return redirect('/social/News')
    else:
        context = {
            'form': form,
            'newses': News.objects.all().order_by('-date'),
        }
    return render(request, "social/news.html", context)
@login_required
def events(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/social/Event')
        else:
            print("envalid")
            return redirect('/social/Event')
    else:
        context = {
            'form': form, 
            'events': Event.objects.all().order_by('-start_date')     
        }
    return render(request, "social/events.html", context)

def delete_events(request, pk):
    enents = get_object_or_404(Event, pk=pk)
    enents.delete()
    return redirect("/social/Event")
