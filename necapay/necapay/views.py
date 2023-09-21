from django.shortcuts import render, redirect

def home(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'index.html', {'user':user})
    return render(request, 'index.html')