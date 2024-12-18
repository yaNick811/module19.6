from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Buyer, Game, News
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html')

def games(request):
    games_list = Game.objects.all()
    return render(request, 'games.html', {'games_list': games_list})

def cart(request):
    return render(request, 'cart.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']

            # Проверяем, существует ли пользователь с таким именем
            if not Buyer.objects.filter(name=username).exists():
                Buyer.objects.create(name=username, balance=0.0, age=age)
                return redirect('index')
            else:
                return render(request, 'registration.html', {'form': form, 'error': 'Пользователь с таким именем уже существует'})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def news(request):
    all_news = News.objects.all().order_by('-date')

    paginator = Paginator(all_news, 5)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'news': page_obj,
    }

    return render(request, 'task1/news.html', context)