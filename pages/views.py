from django.shortcuts import render, redirect
import requests
import json
import requests
from django.http import HttpResponse
from django.http import JsonResponse
from .models import UserProfile
import random
import sys


# Create your views here.


# def index(request, userid):
#     # CUISIN

#     u = Profile.objects.filter(id=userid)
#     cuisin = u[0].Cuisine
#     print(cuisin)
#     # s = cuisin.replace(',', '')
#     c = " ".join(str(cuisin).split(','))
#     print(c)
#     url = "http://15.206.252.9:5000/api/v1.0/dining"

#     payload = {'preference': c}

#     headers = {
#         'Content-Type': 'application/json'
#     }
#     cuisin = requests.post(url, headers=headers, data=json.dumps(payload))
#     # return JsonResponse(list(cuisin.values()), safe=False)
#     cuisin = cuisin.json()

#     # HOTEL
#     hotelurl = "http://15.206.252.9:5000/api/v1.0/hotel"

#     Lifestyle = u[0].Lifestyle
#     print(Lifestyle)
#     hotelpayload = {'preference': 'Manvar Desert Camp'}
#     headers = {
#         'Content-Type': 'application/json'
#     }

#     hotelresponse = requests.post(
#         hotelurl, headers=headers, data=json.dumps(hotelpayload))

#     hotel = hotelresponse.json()

#     # TRAVEL

#     with open('C:/Users/akhan.extern/Desktop/jsondata/attraction_category_modified.json') as f:
#         attraction_dict = json.load(f)

#     attrurl = "http://15.206.252.9:5000/api/v1.0/attraction"

#     travel = u[0].Travel
#     attract_res = []
#     for row in str(travel).split(','):
#         attraction = row.strip()

#         attraction_title = random.choice(attraction_dict[attraction])

#         payloads = {'preference': attraction_title}
#         headers = {'Content-Type': 'application/json'}

#         # print(json.dumps(payloads))
#         travlresponsee = requests.post(
#             attrurl, headers=headers, data=json.dumps(payloads))
#         x = travlresponsee.json()
#         attract_res = attract_res + x['results']['recommendation']
#     # return HttpResponse(attract_res)
#     print(attract_res)


# # cuisin = json.loads(response.text)
#     context = {
#         'cuisin': cuisin,
#         'travel': attract_res,
#         'hotel': hotel,
#     }
#     return render(request, 'pages/index.html', context)
# return JsonResponse(response, safe=False)


def home(request):
    return render(request, 'pages/home.html')


def profile(request):
    if request.method == 'POST':

        # Get form values

        Cuisine = request.POST.getlist('Cuisine[]')

        Lifestyle = request.POST.getlist('Lifestyle[]')

        Travel = request.POST.getlist('Travel[]')

        hotel = request.POST.getlist('Hotel[]')

        user_id = request.user.id
        c = ','.join(Cuisine)
        l = ','.join(Lifestyle)
        t = ','.join(Travel)
        h = ','.join(hotel)
        print(h)
        print(', '.join(Cuisine))
        print(c)
        print(l)
        print(t)
        print(Cuisine)
        print(Lifestyle)
        print(Travel)

        user = UserProfile.objects.filter(user_id=request.user.id).update(
            Cuisine=c, Lifestyle=l, Travel=t, Hotel=h)
        return redirect('recom')
    else:
        return render(request, 'pages/profile.html')


def recom(request):
    u = UserProfile.objects.filter(user_id=request.user.id)
    print(u)
    cuisin = u[0].Cuisine
    print(cuisin)
    # s = cuisin.replace(',', '')
    c = " ".join(str(cuisin).split(','))
    print(c)
    url = "http://15.206.252.9:5000/api/v1.0/dining"

    payload = {'preference': c}

    headers = {
        'Content-Type': 'application/json'
    }
    cuisin = requests.post(url, headers=headers, data=json.dumps(payload))
    # return JsonResponse(list(cuisin.values()), safe=False)
    cuisin = cuisin.json()

    # HOTEL

    with open('C:/Users/akhan.extern/Desktop/jsondata/hotel_category.json', encoding="ISO-8859-1") as h:
        hotel_dict = json.load(h)

    hotelurl = "http://15.206.252.9:5000/api/v1.0/hotel"

    Lifestyle = u[0].Hotel
    hotel_res = []
    for row in str(Lifestyle).split(','):
        cat = row.strip()

        cat_title = random.choice(hotel_dict[cat])

        payloads = {'preference': cat_title}
        headers = {'Content-Type': 'application/json'}

        # print(json.dumps(payloads))
        hotelresponsee = requests.post(
            hotelurl, headers=headers, data=json.dumps(payloads))
        x = hotelresponsee.json()
        hotel_res = hotel_res + x['results']['recommendation']
    # print(hotel_res)

    # TRAVEL

    with open('C:/Users/akhan.extern/Desktop/jsondata/attraction_category_modified.json') as f:
        attraction_dict = json.load(f)

    attrurl = "http://15.206.252.9:5000/api/v1.0/attraction"

    travel = u[0].Travel
    attract_res = []
    for row in str(travel).split(','):
        attraction = row.strip()

        attraction_title = random.choice(attraction_dict[attraction])

        payloads = {'preference': attraction_title}
        headers = {'Content-Type': 'application/json'}

        # print(json.dumps(payloads))
        travlresponsee = requests.post(
            attrurl, headers=headers, data=json.dumps(payloads))
        x = travlresponsee.json()
        attract_res = attract_res + x['results']['recommendation']
     # return HttpResponse(attract_res)
    # print(attract_res)

    # lifestyle
    with open('C:/Users/akhan.extern/Desktop/jsondata/lifestyle_category.json', encoding="ISO-8859-1") as life:
        lifesyl_dict = json.load(life)
        print(lifesyl_dict)
    lifesurl = "http://15.206.252.9:5000/api/v1.0/lifestyle"
    life = u[0].Lifestyle
    lifestyle_res = []
    for row in str(life).split(','):
        lifestyle = row.strip()

        lifesyl_title = random.choice(lifesyl_dict[lifestyle])

        payloads = {'preference': lifesyl_title}
        headers = {'Content-Type': 'application/json'}

        # print(json.dumps(payloads))
        liferesponsee = requests.post(
            lifesurl, headers=headers, data=json.dumps(payloads))
        x = liferesponsee.json()
        lifestyle_res = lifestyle_res + x['results']['recommendation']
       # return HttpResponse(lifestyle_res)
    # print(lifestyle_res)

 # cuisin = json.loads(response.text)
    context = {
        'cuisin': cuisin,
        'travel': attract_res,
        'hotel': hotel_res,
        'life': lifestyle_res,
    }
    return render(request, 'pages/recomd.html', context)
