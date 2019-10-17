from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from social.models import Event
from accounts.models import Friend, Profile



@api_view()
def get_username(request):
    username = request.GET.get('username', '')
    users = User.objects.filter(username=username)

    username = []
    for item in users:
        username.append({'username': item.username,})
    data = {
        'username': username,
    }
    return JsonResponse(data)


@api_view()
def get_user_list(request):
    users = User.objects.all()
    user_list = []
    for item in users:
        user_list.append({'username': item.username, 'slug': item.email})
    data = {
        'user_list': user_list,
    }
    return JsonResponse(data)

@api_view()
def get_user_profile(request, pk=None):
    if pk:
        users = User.objects.filter(pk=pk)
    else:
        users = User.objects.filter(username=request.user)
    user_profile = []
    for item in users:
        user_profile.append({'username': item.username, 'email': item.email, 'Name':item.first_name})
    data = {
        'user_profile': user_profile,
    }
    return JsonResponse(data)

@api_view()
def get_events(request):
    event = Event.objects.all()
    events = []
    for item in event:
        events.append({'title': item.title, 'start': item.start_date, 'end': item.end_date, 'backgroundColor': item.event_class})
    data = {
        'events': events,
    }
    return JsonResponse(data)

@api_view()
def current_user_detail(request):
    profile = User.objects.filter(username=request.user)
    profile_detail = []
    for item in profile:
        profile_detail.append({'first_name': item.first_name, 'last_name': item.last_name, 'email': item.email, 'id':item.id})

    user_info = Profile.objects.filter(user=request.user)
    print(user_info)
    for item in user_info:
        profile_detail.append({'profession': item.profession, 'skils': item.skils, 'education': item.education, 'bio': item.bio, 'location': item.location, 'email': item.birth_date})
    
    if (Friend.objects.filter(current_user=request.user)).exists():
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        friend = []
        for item in friends:
            friend.append({'first_name': item.first_name, 'last_name': item.last_name, 'pk':item.pk})
    else:    
        friend = []
    data = {
        'profile_detail': profile_detail,
        'friend': friend,
    }
    return JsonResponse(data)