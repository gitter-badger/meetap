from django.shortcuts import (render, redirect, get_object_or_404 as G404)
from rekruter.models import User
from .models import (
 PageSkin as S, Blog as B,  PageNames as P, RegNames, ProfileNames)
from .forms import ProfileForm
from meetap.settings import LANGUAGES as L
from meetap.core.classes import (
 PageElement as pe, PageLoad, ActivePageItems)
import pytz
import datetime


# Strona główna.
def home(request):
    api = ActivePageItems(request, B, pytz, datetime)
    active_blogs = api.active_items
    context = {
     'blogs': active_blogs,
     }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/home.html'
    return render(request, template, context_lazy)


# Wszystkie aktualności.
def allblogs(request):
    # pe_b = pe(B)
    api = ActivePageItems(request, B, pytz, datetime)
    active_blogs = api.active_items
    context = {
     'blogs': active_blogs, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/allblogs.html'
    return render(request, template, context_lazy)


# Pojedyńcze aktualności w zbliżeniu.
def blog(request, blog_id):
    pe_b = pe(B)
    pe_b_id = pe_b.by_id(
     G404=G404, id=blog_id)
    context = {
     'blog': pe_b_id, }
    pl = PageLoad(P, L)
    context_lazy = pl.lazy_context(
     skins=S, context=context)
    template = 'strona/blog.html'
    return render(request, template, context_lazy)


# Login Required
# Strona ustawień profilu
def myprofile(request):
    userdata = User.objects.get(
     id=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=userdata)
        if form.is_valid():
            form.save()
            return redirect('myprofile')
    else:
        form = ProfileForm(instance=userdata)
        regitem = pe(RegNames).baseattrs
        profileitem = pe(ProfileNames).baseattrs
        context = {
         'udata': userdata,
         'form': form,
         'regitem': regitem,
         'profileitem': profileitem,
         }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'forms/myprofile.html'
        return render(request, template, context_lazy)


def myprofiledelete(request):
    userdata = User.objects.get(
     id=request.user.id)
    if request.method == 'POST':
        userdata.delete()
        return redirect('home')
    else:
        form = ProfileForm(instance=userdata)
        regitem = pe(RegNames).baseattrs
        profileitem = pe(ProfileNames).baseattrs
        context = {
         'udata': userdata,
         'form': form,
         'regitem': regitem,
         'profileitem': profileitem,
         }
        pl = PageLoad(P, L)
        context_lazy = pl.lazy_context(skins=S, context=context)
        template = 'forms/myprofiledelete.html'
        return render(request, template, context_lazy)
