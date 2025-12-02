from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def ai_challenge(request):
    return render(request, 'ai-challenge.html')

def user_challenge(request):
    return render(request, 'user-challenge.html')