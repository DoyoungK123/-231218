from django.shortcuts import render
from eggtart.models import Eggtart

def main(request):
    return render(request, "main.html")

def eggtart_list(request):
    eggtart = Eggtart.objects.all()
    print("전체 에그타르트 맛집 목록:", eggtart)

    context = {
        "eggtart": eggtart,
    }

    return render(request, "eggtart_list.html", context)

def eggtart_search(request):
    keyword = request.GET.get("keyword")

    if keyword is not None:

        eggtart = Eggtart.objects.filter(shop__contains=keyword)

    else:

        eggtart = Eggtart.objects.none()

    context = {
        "eggtart": eggtart,
    }
    return render(request, "eggtart_search.html", context)