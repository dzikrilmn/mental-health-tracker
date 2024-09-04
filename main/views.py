from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306275544',
        'name': 'Muhammad Dzikri Ilmansyah',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
