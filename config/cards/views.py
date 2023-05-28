from django.contrib.sites import requests
from django.shortcuts import render, get_object_or_404
from .models import Cards
# Create your views here.
def view_cards(request, pk=None) -> render:
    if pk:
        current_card = get_object_or_404(Cards, pk=pk)
        template = 'card_detail.html'
        context = {
            'current_card': current_card,
        }
    else:
        cards = Cards.objects.all()
        template = 'cards.html'
        context = {
            'cards': cards,
        }

    return render(request=request, template_name=template, context=context)


def fake_api(request):
    # Получение данных с API
    # try:
    #     response = requests.get('https://github.com/Mirzoahmad/coder')
    #     data = response.json()
    # except Exception as e:
    #     print(e)
    #     data = {'https://github.com/Mirzoahmad/coder'}
    # print(data)
    fake_info = {
        "name": "MirzoAhmad",
        "surname": "Nazaraliev",
        "link": "https://github.com/Mirzoahmad/coder"
    }
    # Передача данных в шаблон
    return render(request, 'get_api.html', {'data': fake_info})