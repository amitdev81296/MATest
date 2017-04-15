from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'StreamAnalysis/home.html', context)
