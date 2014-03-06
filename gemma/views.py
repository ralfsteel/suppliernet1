from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse


from gemma.forms import UserForm, UserProfileForm, PricelistForm, PromotionalForm, PricelistMain, PricelistMainForm
from gemma.models import Pricelist, Promotional


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save()
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }

    return render_to_response('gemma/register.html', context_dict, context)


def login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Login Succesful")
        else:
            return HttpResponse("Invalid detail")

    return render_to_response('gemma/login.html', context)





def pricelist(request, plist_pk):
    plist = PricelistMain.objects.get(pk=plist_pk)
    files = Pricelist.objects.filter(plist=plist_pk).order_by('-created')

    context = RequestContext(request)
    if request.method == 'POST':
        form = PricelistForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = Pricelist(pricelist_detail=request.FILES['pricelist_detail'], pricelist_name=request.POST['pricelist_name'])
            new_file.save()

            return HttpResponseRedirect(reverse('gemma.views.pricelist'))

    else:
            form = PricelistForm()

    if request.method == 'POST' and request.POST.get('pricelist_name'):
        pricelist_name = request.POST['pricelist_name']
        Pricelist.objects.filter(pricelist_name=pricelist_name).delete()

    #pricelists = Pricelist.objects.all().order_by('-created')
    context_dict = {
        'form': form,
        #'pricelists': pricelists,
        'plist': plist,
        'files': files

    }

    return render_to_response('gemma/pricelist.html', context_dict, context)

def main_pricelist(request):
     context = RequestContext(request)
     if request.method == 'POST':
        form = PricelistMainForm(request.POST)
        if form.is_valid():
            new_file = PricelistMain(name=request.POST['name'])
            new_file.save()
            return HttpResponseRedirect(reverse('gemma.views.main_pricelist'))
     else:
        form = PricelistMainForm()

     lists = PricelistMain.objects.all().order_by('-date')
     context_dict = {
        'form': form,
        'lists': lists
     }

     return render_to_response('gemma/main_pricelist.html', context_dict, context)




def promotional(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PromotionalForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = Promotional(promotional_detail=request.FILES['promotional_detail'], promotional_name=request.POST['promotional_name'])
            new_file.save()

            return HttpResponseRedirect(reverse('gemma.views.promotional'))

    else:
            form = PromotionalForm()

    if request.method == 'POST' and request.POST.get('promotional_name'):
        promotional_name = request.POST['promotional_name']
        Promotional.objects.filter(promotional_name=promotional_name).delete()

    promotionals = Promotional.objects.all().order_by('-created')
    context_dict = {
        'form': form,
        'promotionals': promotionals,

    }

    return render_to_response('gemma/promotional.html', context_dict, context)






