from lib2to3.fixes.fix_input import context

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

def burger_search(request):
    keyword = request.GET.get("keyword")

    # keyword가 주어진 경우
    if keyword:
        burgers = Burger.objects.filter(name__contains=keyword)
    # keyword가 없는 경우, 즉 주소표시줄에 keyword가 없어 None을 반환한 경우
    else:
        burgers = Burger.objects.none()

    contexts = {
        "burgers": burgers,
    }
    return render(request, "burger_search.html", contexts)