from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import generator

import jwt

secret_key='shdbcwdbuce'


# Create your views here.
def dashboard(request):
    # payment_data = request.POST.get('amount')
    # encoded_token = jwt.encode(payment_data, secret_key, algorithm="HS256")
    # return HttpResponse('Welcome, we have been expecting you 😈')
    user = request.user
    if user.is_authenticated:
        return render(request, 'dashboard.html', {'user': user})
    else:
        return redirect('/accounts/login')

@login_required
def generate(request):
    if request.method == 'POST':
        commodity = request.POST.get('commodity', '')
        amount = float(request.POST.get('amount', ''))
        user = request.user

        account_balance = float(user.amount)
        if account_balance < amount :
            messages.error(request, 'Insufficient balance')
            return render(request, 'generate.html')

        print(type(user), 'it is well')
        
        data = {
            'commodity' : commodity,
            'amount' : amount,
        }

        result = generator.generate(data)
        request.user.amount = float(request.user.amount) - amount
        request.user.save()
        return render(request, 'generate.html', {'token': result})

    else:
        return render(request, 'generate.html')

@login_required
def verify(request):
    if request.method == 'POST':
        commodity = request.POST.get('commodity', '')
        token = request.POST.get('token', '')
        

        result = generator.verify(token)
        if result:
            request.user.amount = float(request.user.amount) + result
            request.user.save()
            return HttpResponse(f'Transaction successful! {result} was credited into the account!')
        else:
            
            return HttpResponse(f'Transaction unsuccessful! Try again')
        

    else:
        return render(request, 'verify.html')