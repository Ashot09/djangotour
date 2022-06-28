from unicodedata import category
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import CategoryStays, HomeBG, NextTourPlace, OfferGoods, TourIdea, SwipeReserve, Thinks, Info1, Info2
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homebg = HomeBG.objects.all()
        tour = TourIdea.objects.all()
        offer = OfferGoods.objects.all()
        reserve = SwipeReserve.objects.all()
        thinks = Thinks.objects.all()
        place = NextTourPlace.objects.all()

        return render(request, self.template_name, {'homebg':homebg, 'tour':tour, 'offer':offer, 'reserve':reserve, 'thinks':thinks, 'place':place})


class AboutListView(ListView):
    template_name = 'aboutus.html'

    def get(self, request):
        info1 = Info1.objects.all()
        info2 = Info2.objects.all()
        return render(request, self.template_name, {'info1':info1, 'info2':info2})


class StaysListView(ListView):
    template_name = 'stays.html'

    def get(self, request):
        rentsell = CategoryStays.objects.all()
        
        return render(request, self.template_name, {'rentsell':rentsell})
