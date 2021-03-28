from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

from django.views.decorators.http import require_GET, require_POST, require_safe, require_http_methods

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


@require_http_methods(['GET','POST'])
def signup(request):
    # authenticated: 로그인 되있는지 아닌지만 판단
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)
            


# 1. 이미 로그인 되있는지 확인
# 2. 로그인이 안되있으면 POST 확인
# 3. 
@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # form.get_user 메서드를 통해 id 및 패스워드만 전달
            auth_login(request, form.get_user())
            # next_url ***
            next_url = request.GET.get('next')
            return redirect(next_url or 'community:index')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

    
@login_required
@require_GET
def logout(request):
    auth_logout(request)
    return redirect('community:index')