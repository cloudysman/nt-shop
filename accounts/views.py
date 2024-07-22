from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomAuthenticationForm, SignUpForm

def home_view(request):
    return render(request, 'accounts/shop.html') 

def get_navbar_context(request):
    context = {
        'user_is_authenticated': request.user.is_authenticated
    }
    return context

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"User {username} logged in successfully.")
                return redirect('shop')  
            else:
                print(f"Authentication failed for user {username}.")
                messages.error(request, "Tên đăng nhập hoặc mật khẩu không hợp lệ.")
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không hợp lệ.")
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form
    }
    context.update(get_navbar_context(request))
    return render(request, 'accounts/login.html', context)

def shop_view(request):
    context = get_navbar_context(request)
    return render(request, 'accounts/shop.html', context)  

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1']) 
            user.save()
            messages.success(request, "Đăng ký thành công. Vui lòng đăng nhập.")
            return redirect('login') 
        else:
            messages.error(request, "Đăng ký không thành công.")
            print(form.errors)  
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    context.update(get_navbar_context(request))
    return render(request, 'accounts/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
