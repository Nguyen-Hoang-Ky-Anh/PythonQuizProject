"""
URL configuration for PythonQuizProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from quizzes import views as quiz_views
from django.urls import include, path

def home(request):
    return HttpResponse("Trang chủ Quiz Project!")

urlpatterns = [
    path('admin/', admin.site.urls),

    # Trang chủ
    path('', quiz_views.home, name='home'),

    # Quiz views
    path('ai-challenge/', quiz_views.ai_challenge, name='ai-challenge'),
    path('user-challenge/', quiz_views.user_challenge, name='user-challenge'),
    path('home/', quiz_views.login, name='login'),
    path('login/', quiz_views.register, name='register'),

    # Include app ai_assistant
    path('assistant/', include('ai_assistant.urls')),
]
