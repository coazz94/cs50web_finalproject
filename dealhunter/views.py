from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .models import *

CATEGORIES = ["Elektronik", "Gaming", "Fashion", "Beauty", "Food", "Home and Living"]

# Create your views here.

def index(request):

    deals = Deal.objects.all()

    return render(request, "dealhunter/index.html", {
        "categories" : CATEGORIES, 
        "deals" : deals
    })

def new_deal(request):

    if request.method == "POST":
        deal_url = request.POST["deal_url"]
        heading = request.POST["heading"]
        description = request.POST["description"]
        price = request.POST["price"]
        # TODO adjust the date so that it fits the date format in django db
        s_date = request.POST["s_date"]
        e_date = request.POST["e_date"]
        d_code = request.POST["d_code"]
        category = request.POST["category"]
        img_url = request.POST["img_url"]

        user = User.objects.get(id=request.user.id)
        print(user)
        #try:
        deal = Deal(
            creator=user,
            url=deal_url,
            heading=heading,
            description=description,
            price=price,
            start_date=s_date,
            end_date=e_date,
            category=category,
            d_code=d_code,
            image_url=img_url
            )
        deal.save()
        #except IntegrityError:
        #    return render(request, "dealhunter/newdeal.html", {
        #        "message": "Error occured while creating the Deal, try again"
        #    })   

    return render(request, "dealhunter/newdeal.html",{
        "options": CATEGORIES
    })


def login(request):

    if request.method == "POST":

        # Try to sign in the user
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)


        # Check if authentication successful
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "dealhunter/login.html", {
                "message": "Invalid username and/or password."
            })

    # If not POST than display the login view
    return render(request, "dealhunter/login.html")


def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]

        # Ensure password matches repeated confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "dealhunter/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            user.save()
        except IntegrityError:
            return render(request, "dealhunter/register.html", {
                "message": "Username already taken."
            })
        auth_login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "dealhunter/register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def dealview(request, deal_id):

    deal = Deal.objects.get(id=deal_id)

    return render(request, "dealhunter/dealview.html", {
        "deal" : deal
    })

def profileview(request, profile_id):

        profile = User.objects.get(id=request.user.id)

        return render(request, "dealhunter/profileview.html", {
        "profile" : profile
    })