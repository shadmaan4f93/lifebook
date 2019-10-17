from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UpdateProfile, UserInfoForm
from django.contrib.auth import update_session_auth_hash
from .forms import RegistrationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from skflite import settings
from django.core.mail import EmailMessage
from .models import Friend, Profile

#------------------------------------------------------------------------------------------

def accounts_settings(request):
    return render(request, "accounts/account_settings.html")

def general_settings(request):
    return render(request, "accounts/general_settings.html")

#-------------------------------------------------------------------------------------------
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.INFO, 'This username is allready exist')
            form = RegistrationForm()
            return redirect('/accounts/signup/')
        else:
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                current_site = get_current_site(request)
                subject = 'Activate your LIFEBOOK account.'
                message = render_to_string('acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': user.pk,
                    'token':account_activation_token.make_token(user),
                })
                from_email = settings.EMAIL_HOST_USER
                to_email = form.cleaned_data.get('email')
                msg = EmailMessage(subject, message, from_email, [to_email])
                msg.content_subtype = "html"
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('/') 
                # msg.send()      
                # return render(request, 'accounts/signup_conform.html') 
                                            
            else:
                form = RegistrationForm()
                return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

#---------------------------------------------------------------------------------------------

def activate(request, uidb64, token):
    uid = uidb64
    user = User.objects.get(pk=uid)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.add_message(request, messages.INFO, 'Thank you for your email confirmation.')
        return redirect('/')
    else:
        return HttpResponse('Activation link is invalid!')
#---------------------------------------------------------------------------------------------
@login_required
def edit_profile(request):
    if request.method == 'POST':    
        form = ProfileUpdateForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('accounts/profile/edit/')
    else:
        form = ProfileUpdateForm(instance = request.user)
       
    return render(request, 'accounts/edit_profile.html', {'form':form})

#---------------------------------------------------------------------------------------------
@login_required
def add_user_info(request):
    if request.method == 'POST':    
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            messages.add_message(request, messages.INFO, 'Congratulations yor information has been added to your profile')
            return redirect('/accounts/user/profile/')
        else:
            messages.add_message(request, messages.INFO, 'Something wrong')
            return redirect('/accounts/user/profile/add/')
    else:
        form = UserInfoForm()
       
    return render(request, 'accounts/user_info_update.html', {'form':form})


#---------------------------------------------------------------------------------------------
@login_required
def update_user_info(request):
    if request.method == 'POST':    
        form = UserInfoForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Congratulations your profile hase been updated')
            return redirect('/accounts/user/profile/')
        else:
            messages.add_message(request, messages.INFO, 'Something wrong')
            return redirect('/accounts/user/profile/update/')
    else:
        form = UserInfoForm(instance=request.user.profile)
       
    return render(request, 'accounts/user_info_update.html', {'form':form})

#--------------------------------------------------------------------------------------------
@login_required
def profile(request):
    user = request.user
    if (Friend.objects.filter(current_user=request.user)).exists():
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    else:
        friends=[]
    args = {
        'user': user,
        'friend': friends
    }    
    return render(request, 'accounts/profile.html', args)

#--------------------------------------------------------------------------------------------
@login_required
def friend_profile(request, pk=None):
    user = User.objects.filter(pk=pk)
    users = User.objects.get(pk=pk)
    if (Friend.objects.filter(current_user=users)).exists():
        friend = Friend.objects.get(current_user=users)
        friends = friend.users.all()
    else:
        friends=[]
    args = {
        'user': user,
        'friend': friends
    }    
    return render(request, 'accounts/friend_profile.html', args)  
#-----------------------------------------------------------------------------------------------
@login_required
def change_password(request):
    args = {}
    if request.method == 'POST':    
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/Home/')
        else:
            return redirect('accounts/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args['form'] = form
    return render(request, 'accounts/change_password.html', args)

#-----------------------------------------------------------------------------------------------

def change_friend(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, new_friend)
    elif operation == 'conform':
        Friend.conform_friend(request.user, new_friend)
    return redirect('/')

# def addFriend(request, operation, pk):
#     new_friend = User.objects.get(pk=pk)
#     if operation == 'add':
#         FriendsData.addFriends(request.user, new_friend)
#     elif operation == 'remove':
#         FriendsData.removeFriends(request.user, new_friend)
#     return redirect('/')