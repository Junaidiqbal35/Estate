from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Inbox

from django.contrib import messages
from . import forms
from django.core.mail import send_mail


# Create your views here.
def contact(request):
    if request.method == 'POST':

        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        host_id = request.POST['host_id']
        host_email = request.POST['host_email']

        # check if user has made inquiry alreaady

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'you have already made an inquiry for this listing')
                return redirect('index')

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                          user_id=user_id, host_email=host_email, host_id=host_id)
        contact.save()

        from django.core.mail import send_mail

        send_mail(
            'Event Space Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the gmail for more info',
            'junaidiqbal0323@gmail.com',
            [host_email, 'mc130202861@vu.edu.pk'],
            fail_silently=False,
        )

        messages.success(request, 'your request has been submitted, a host will get back to you soon')
        return redirect('index')


def mycontact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        message = request.POST['message']
        sender = request.POST['sender']
        receiver = request.POST['receiver']

        # check if user has made inquiry alreaad

        contact = Inbox(listing=listing, message=message, sender=sender, receiver=receiver)
        contact.save()
        messages.success(request, 'your request has been submitted, a host will get back to you soon')
        return redirect('index')


def message(request, id):
    contact = get_object_or_404(Contact, pk=id)
    reply_form = forms.ReplyMesaageForm(request.POST)

    if request.method == 'POST':
        if reply_form.is_valid():

            listing = request.POST.get('listing')
            listing_id = request.POST.get('listing_id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            host_email = request.POST.get('host_email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            user_id = request.POST.get('user_id')
            host_id = request.POST.get('host_id')
            reply_id = request.POST.get('contact_id')
            reply_qs = None
            if reply_id:
                reply_qs = Contact.objects.get(id=reply_id)
            reply = Contact.objects.create(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                                           message=message, user_id=user_id, host_email=host_email, host_id=host_id,
                                           reply=reply_qs)
            reply.save()
            return redirect('message', id=contact.pk)
    else:
        reply_form = forms.ReplyMesaageForm()

    context = {

        'contacts': contact,
        'form': reply_form,

    }
    return render(request, 'contact/reply.html', context)


def receive(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(host_id=request.user.id, reply=None)

    context = {

        'contacts': user_contacts,

    }
    return render(request, 'contact/receive.html', context)
