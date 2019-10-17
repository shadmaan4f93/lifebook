import socket

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, EmailMessage, send_mail
from django.shortcuts import HttpResponse, redirect, render
from django.views.generic import TemplateView

import requests
from accounts.models import Friend
from bs4 import BeautifulSoup
from skflite import settings
from social.forms import UserPostForm
from social.models import UserPost

from .forms import ContactForm, QuestionForm, ReviewForm, ScrapyForm
from .models import Question, Subject


def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)


@login_required
def test(request):


    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_address = ('localhost', 10000)
    # client.bind(server_address)
    # #streamurl = '(ws://streamer-bin.tdameritrade.com)'
    # # ip = socket.getaddrinfo ("ws://echo.websocket.org/", 80)
    # con = client.connect(("127.0.0.1",10000))
    # con.send('thanks')
    #addreinfo = socket.getaddrinfo('localhost', 8000)
    if request.method == 'POST':
        form = ScrapyForm(request.POST)
        if form.is_valid(): 
            url = form.cleaned_data['url']
            element = form.cleaned_data['element']  
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            p=soup.find(element)
            s=soup.find_all(class_=""+element+"")
            return HttpResponse(s)                                                                 
    else:
        form = ScrapyForm()
    return render(request, "test.html", {
        'form': form
    })
    

@login_required
def index(request):
    if request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.posted_by = request.user
            post.save()
    else:
        form = UserPostForm()
    if(Friend.objects.filter(current_user=request.user, status=True)).exists():
        friend = Friend.objects.get(current_user=request.user )
        friends = friend.users.all()
    else:
        friends=[]
    context = {
    'form': form,
    'Friends': friends,
    'Post': UserPost.objects.all(),
    }
    return render(request, "home.html", context)

@login_required
def about(request):
    return render(request, "about.html")

@login_required
def members(request):
    context = {
    'members': User.objects.exclude(id=request.user.id),
    }
    return render(request, "members.html", context)

def question_upload(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = QuestionForm()
    return render(request, 'home/Question_upload.html', {
        'form': form
    })

@login_required
def feedback(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print('form valid')
            subject = 'Feedback from site'
            html_content = (
                '<h4>You have received a new message from the contact us form on your website</h4><br/>'
                '<strong>Email: </strong>' + form.cleaned_data['email'] + '<br/>'
                '<strong>Phone: </strong>' + form.cleaned_data['phone'] + '<br/>'
                '<strong>Comments: </strong>' + form.cleaned_data['comments'] + ''
            )
            from_email = settings.EMAIL_HOST_USER
            to = [settings.ADMINS[0][1]]
            print(to)
            print(from_email)
            try:
                msg = EmailMessage(subject, html_content, from_email, to)
                msg.content_subtype = "html"
                msg.send()
                print('message send')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return redirect('/feedback')  
    else:
        form = ReviewForm()
    return render(request, 'feedback.html', {'form': form})
