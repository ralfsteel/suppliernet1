from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse

from gemma.forms import RegisterForm, LoginForm, PricelistForm
from gemma.models import Pricelist


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            registered = True
        else:
            print form.errors
    else:
        form = RegisterForm()

    context_dict = {
        'form': form,
        'registered': registered
    }

    return render_to_response('gemma/register.html', context_dict, context)


def login(request):
    context = RequestContext(request)
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("logged in")
            else:
                return HttpResponse("Invalid Data")

    context_dict = {
        'form': form,

    }

    return render_to_response('gemma/login.html', context_dict, context)

def pricelist(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PricelistForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = Pricelist(pricelist_detail=request.FILES['pricelist_detail'])
            new_file.save()

            return HttpResponseRedirect(reverse('gemma.views.pricelist'))
    else:
            form = PricelistForm()

    pricelists = Pricelist.objects.all()

    context_dict = {
        'form': form,
        'pricelists': pricelists
    }

    return render_to_response('gemma/pricelist.html', context_dict, context)





