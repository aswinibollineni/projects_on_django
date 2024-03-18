from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import AddQuestionForm
from .models import Question

def home(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        score, wrong, correct, total = 0, 0, 0, 0

        for q in questions:
            total += 1
            selected_answer = request.POST.get(str(q.id))  # Use the ID of the question as the key

            if selected_answer == q.correct_answer:
                score += 10
                correct += 1
            else:
                wrong += 1

        percent = (score / (total * 10)) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'Quiz/result.html', context)
    else:
        questions = Question.objects.all()
        context = {'questions': questions}
        return render(request, 'Quiz/home.html', context)

def add_question(request):
    if request.method == 'POST':
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddQuestionForm()
    return render(request, 'Quiz/add_question.html', {'form': form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Add error message or handle invalid login
            pass

    return render(request, 'Quiz/login.html')

def logout_page(request):
    logout(request)
    return redirect('home')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'Quiz/register.html', {'form': form})
