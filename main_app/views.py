from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def main_page(request):
    return render(request, 'second_index.html')


def one_page(request):
    return render(request, 'fourth_index.html')


def second_page(request):
    return render(request, 'fifth_index.html')


def third_page(request):
    return render(request, 'sixth_index.html')
# Create your views here.
