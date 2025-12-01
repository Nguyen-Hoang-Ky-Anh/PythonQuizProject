# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LearnerSignUpForm
from .models import User

# Tạm thời dùng AI test mock
def ai_level_test(learner):
    """
    Giả lập test AI.
    Input: learner (User object)
    Output: recommended_level
    """
    # Ở đây tạm random hoặc dựa vào declared_level để test
    import random
    levels = ['Beginner', 'Elementary', 'Pre-intermediate', 'Intermediate', 'Upper-intermediate', 'Advanced']
    recommended = random.choice(levels)
    return recommended

def signup_view(request):
    if request.method == 'POST':
        form = LearnerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'learner'
            user.save()
            
            # AI test
            if user.declared_level != 'Beginner':
                recommended_level = ai_level_test(user)
                # lưu tạm recommended_level vào session
                request.session['recommended_level'] = recommended_level
                return redirect('level_test_result')  # trang thông báo kết quả
            else:
                login(request, user)
                return redirect('home')
    else:
        form = LearnerSignUpForm()
    return render(request, 'users/signup.html', {'form': form})
