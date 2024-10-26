from django.shortcuts import render
from burgers.models import Burger

def main(request):
    return render(request, "main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    context = {
        "burgers":burgers,
    }
    return render(request, "burger_list.html", context)

