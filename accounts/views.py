from django.shortcuts import render, redirect, get_object_or_404
from  django.contrib import  messages, auth
from  django.contrib.auth.models import User
from django.contrib import messages




from .models import Profile
from . import forms
#from django.contrib.auth.forms import UserCreationForm
#from host.models import UserProfile
from .forms import UserRegistrationForm
from contacts.models import Contact
from django.core.validators import validate_email


# Create your views here
def register1(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user= form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')



            user.save()
            Profile.objects.create( user= user)
            messages.success(request, 'you are now registered and can log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register1.html', {'form':form})

def register(request):

    if request.method == 'POST':
        # get form values

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if password match


        if password == password2:
            # Check UserName
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username is taken')
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email is  already in used!!')
                    return redirect('register')

                else:
                    #all good

                    user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name ,email=email )
                    # login after register
                    user.save()
                    Profile.objects.create(user = user)
                    messages.success(request,'you are now registered and can log in')
                    return redirect('login')

        else:
            messages.error(request,'Passwords do not match ')


        return  redirect('register')

    else:

        return render (request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')




        return redirect('register')

    else:

        return render (request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'you are now logged out')
        return redirect('index')


    return redirect('index')


def dashboard(request):

    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)

    context = {

        'contacts': user_contacts,

    }
    return render (request, 'accounts/dashboard.html', context)

def receive(request):


    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id, reply= None)

    context = {

        'contacts': user_contacts,

    }
    return render (request, 'accounts/receive.html', context)



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
            reply = Contact.objects.create(listing=listing, listing_id = listing_id, name = name, email=email, phone=phone, message = message, user_id=user_id, host_email=host_email,host_id=host_id, reply = reply_qs)
            reply.save()
            return redirect('message', id=contact.pk)
    else:
        reply_form = forms.ReplyMesaageForm()


    context = {

        'contacts': contact,
        'form': reply_form,

    }
    return render (request, 'contact/reply.html', context)





def profile(request):
    profile = Profile.objects.get(user = request.user.id )

    if request.method == 'POST':

        form = forms.ProfileForm(request.POST,files=request.FILES, instance=request.user.profile)
        if form.is_valid():
            #instance = form.save(commit=False)
            form.save()
            return redirect('dashboard')

    else:
        form = forms.ProfileForm(instance=request.user.profile)

    context = {

        'form': form,
        'profile': profile,

    }

    return render(request, 'accounts/profile.html', context)




