from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from host.models import Host

from listings.choices import price_choices, title_choices, state_choices, city_choices


# Create your views here.

def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'city_choices': city_choices,
        'title_choices': title_choices,
        'price_choices': price_choices,

    }
    return render(request, 'pages/index.html', context)


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    hostings = Host.objects.order_by('-hire_date')

    # get MVP
    mvp_hostings = Host.objects.all().filter(is_mvp=True)

    context = {
        'hostings': hostings,
        'mvp_hostings': mvp_hostings
    }
    return render(request, 'pages/about.html', context)
