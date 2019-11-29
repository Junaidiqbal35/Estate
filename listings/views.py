from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import HttpResponseRedirect

from django.contrib import messages

from . import forms

from django.contrib.auth.decorators import login_required

from django.contrib import messages, auth

from django.shortcuts import render, get_object_or_404, redirect
from listings.choices import city_choices, price_choices, title_choices, state_choices
from .models import Listing, Comment

from django.utils import timezone


# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)

    page = request.GET.get('page')

    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def myindex(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True, ).annotate(
        avg_review=Avg('rates__rating'))
    paginator = Paginator(listings, 3)

    page = request.GET.get('page')

    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, id):
    # listings = Listing.objects.order_by('-list_date').filter(is_published=True,).annotate(avg_review=Avg('rates__rating'))
    listing = get_object_or_404(Listing, pk=id)
    comments = Comment.objects.filter(listing=listing).order_by('-id')

    comment_form = forms.CommentForm(request.POST)
    is_favourite = False
    if listing.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    if request.method == 'POST':
        if comment_form.is_valid():

            content = request.POST.get('content')
            rating = request.POST.get('rating')
            comment = Comment.objects.create(listing=listing, user=request.user, content=content, rating=rating, )

            comment.save()

            return redirect('listing', id=listing.pk)
        else:
            comment_form = forms.CommentForm

    context = {

        'listing': listing,
        'comments': comments,
        'comment_form': comment_form,
        'is_favourite': is_favourite,
    }

    return render(request, 'listings/listing.html', context)


# @login_required(login_url="/accounts/login.html")
def listing1(request, id):
    # listings = Listing.objects.order_by('-list_date').filter(is_published=True,).annotate(avg_review=Avg(
    # 'rates__rating'))
    listing = get_object_or_404(Listing, pk=id)
    comments = Comment.objects.filter(listing=listing).order_by('-id')

    comment_form = forms.CommentForm(request.POST)
    is_favourite = False
    if listing.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    if request.method == 'POST':
        if comment_form.is_valid():

            content = request.POST.get('content')
            rating = request.POST.get('rating')
            comment = Comment.objects.create(listing=listing, user=request.user, content=content, rating=rating, )

            comment.save()

            return redirect('listing', id=listing.pk)
        else:
            comment_form = forms.CommentForm

    context = {

        'listing': listing,
        'comments': comments,
        'comment_form': comment_form,
        'is_favourite': is_favourite,
    }

    return render(request, 'listings/modify_listing.html', context)


def mylisting(request):
    # user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    listings = Listing.objects.filter(host_id=request.user.id)

    context = {

        'listings': listings
    }

    return render(request, 'listings/mylisting.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']

        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    # title
    if 'title' in request.GET:
        title = request.GET['title']

        if title:
            queryset_list = queryset_list.filter(title__iexact=title)

    # city
    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

        # State
    if 'state' in request.GET:
        state = request.GET['state']

        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # price
    if 'price' in request.GET:
        price = request.GET['price']

        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {

        'state_choices': state_choices,
        'title_choices': title_choices,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'listings': queryset_list,
        'values': request.GET,

    }
    return render(request, 'listings/search.html', context)


"""
@login_required
def create(request):

    user = User.objects.all()
    if request.method == 'POST':

        # get form values
        if request.POST['title'] and request.POST['address'] and request.POST['zipcode'] and request.POST['state'] and request.POST['city'] and request.POST['description']  and request.POST['price'] and  request.POST['bedrooms'] and request.POST['bathrooms'] and request.POST['garage'] and request.POST['sqft'] and request.FILES['photo_main'] and request.FILES['photo_1'] and request.FILES['photo_2']:


            listing = Listing()
            listing.title = request.POST['title']
            listing.address = request.POST['address']
            listing.zopcode = request.POST['zipcode']
            listing.state = request.POST['state']
            listing.city = request.POST['city']
            listing.description = request.POST['description']
            listing.price = request.POST['price']
            listing.bedrooms = request.POST['bedrooms']
            listing.bathrooms = request.POST['bathrooms']
            listing.garage = request.POST['garage']
            listing.sqft = request.POST['sqft']
            listing.lot_siz
            ++ = request.POST['lot_size']
            listing.photo_main = request.FILES['photo_main']
            listing.photo_1 = request.FILES['photo_1']
            listing.photo_2 = request.FILES['photo_2']
            listing.list_date = timezone.datetime.now()
            listing.host = request.user

            listing.save()
            return redirect('index')

        else:
             return render(request,'listings/listings.html')
    else:
        return render(request, 'listings/create.html')


"""
"""
def edit(request ,id ):
    listing = Listing.objects.get(id=id)

    return render(request, 'listings/edit_listing.html' , {'listing' : listing})
"""


def update(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == 'POST':
        form = forms.EditListingForm(request.POST or None, files=request.FILES or None, instance=listing)
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.host_id = request.user
            # instance.save()

            form.save()

            return redirect('listing', id=listing.pk)



    else:
        form = forms.EditListingForm(instance=listing)
    context = {
        'listing': listing,
        'form': form,
    }

    return render(request, 'listings/edit_listing.html', context)


def delete(request, id):
    listing = Listing.objects.get(id=id)

    listing.delete()

    return redirect('index')


def addspace(request):
    if request.method == 'POST':

        form = forms.addSpaceForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.host_id = request.user.id
            instance.save()
            messages.success(request, 'you  Space is Successfully Added !!')
            return redirect('index')

    else:
        form = forms.addSpaceForm()

    return render(request, 'listings/addspace.html', {'form': form})


"""
def add_comment_to_listing (request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.listing = listing
            comment.save()
            return redirect('post_detail', pk=listing.pk)
    else:
        form =forms.CommentForm()
    return render(request, 'listings/add_comment_to_listing.html', {'form': form})

"""


def favourite(request, id):
    # if request.method == 'POST':

    listing = get_object_or_404(Listing, id=id)
    # user_board = User.objects.filter(user_id=request.user.id)
    if listing.favourite.filter(id=request.user.id).exists():

        listing.favourite.remove(request.user)

    else:
        listing.favourite.add(request.user)

    return redirect('listing', id=listing.pk)


def board(request):
    user = request.user
    favourite_listing = user.favourite.all()
    context = {
        'favourite_listing': favourite_listing,
    }

    return render(request, 'listings/saveboard.html', context)


def photoShoot_Search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    queryset_list = queryset_list.filter(title__iexact='PhotoShoot')

    context = {

        'state_choices': state_choices,
        'title_choices': title_choices,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'listings': queryset_list,
        'values': request.GET,

    }

    return render(request, 'listings/photoshoot.html', context)


def birthday_Search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    queryset_list = queryset_list.filter(title__iexact='Birthday Party')

    context = {
        'state_choices': state_choices,
        'title_choices': title_choices,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'listings': queryset_list,
        'values': request.GET,

    }

    return render(request, 'listings/birthday_party.html', context)


def workshop_Search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    queryset_list = queryset_list.filter(title__iexact='WorkShop')

    context = {
        'state_choices': state_choices,
        'title_choices': title_choices,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'listings': queryset_list,
        'values': request.GET,

    }

    return render(request, 'listings/workshop.html', context)


def bridalShower_Search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    queryset_list = queryset_list.filter(title__iexact='Bridal Shower')

    context = {
        'state_choices': state_choices,
        'title_choices': title_choices,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'listings': queryset_list,
        'values': request.GET,

    }

    return render(request, 'listings/bridal_shower.html', context)


def meeting_Search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    queryset_list = queryset_list.filter(title__iexact='Meeting')

    context = {
        'state_choices': state_choices,
        'title_choices': title_choices,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'listings': queryset_list,
        'values': request.GET,

    }

    return render(request, 'listings/meeting.html', context)


def wedding_Search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    queryset_list = queryset_list.filter(title__iexact='Wedding Destination')

    context = {
        'state_choices': state_choices,
        'title_choices': title_choices,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'listings': queryset_list,
        'values': request.GET,

    }

    return render(request, 'listings/wedding_destination.html', context)
