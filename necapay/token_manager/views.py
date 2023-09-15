from django.shortcuts import render, HttpResponse
import jwt

secret_key='shdbcwdbuce'


# Create your views here.
def home(request):
    # payment_data = request.POST.get('amount')
    # encoded_token = jwt.encode(payment_data, secret_key, algorithm="HS256")
    return HttpResponse('Welcome, we have been expecting you 😈')

def generate(request):
    # return HttpResponse('generated!!')
    return render(request, 'index.html')


def verify(request):
    return HttpResponse("verified!!")   