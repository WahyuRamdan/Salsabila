from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from app.models import *

def home(request):
    maps = Maps.objects.all()
    tables = Table.objects.all()

    return render(request, 'index.html', context = {
        "maps": maps,
        "tables" : tables
    })

def maps(request):
    maps = Maps.objects.all()
    if request.method == "POST":
        Maps.objects.create(
            kota = request.POST.get("kota"),
            lokasi = request.POST.get("lokasi")
        )

    if request.user.is_authenticated:
        return render(request, "maps.html", context = {
            "maps": maps,
        })
    else:
        return redirect("/login")

def mapsUpdate(request, id):
    maps = Maps.objects.all()
    map_id = Maps.objects.get(id = id)

    if request.method == "POST":
        map_id.kota = request.POST.get("kota")
        map_id.lokasi = request.POST.get("lokasi")
        map_id.save()

    if request.user.is_authenticated:
        return render(request, "maps.html", context = {
            "maps": maps,
            "map_id" : map_id
        })
    else:
        return redirect("/login")


def mapsDelete(request, id):
    if request.user.is_authenticated:
        map_id = Maps.objects.get(id = id)
        map_id.delete()
        return redirect("/maps")
    else:
        return redirect("/login")




def table(request):
    tables = Table.objects.all()
    if request.method == "POST":
        Table.objects.create(
            kota = request.POST.get("kota"),
            ciri_khas = request.POST.get('ciri_khas'),
            provinsi = request.POST.get("provinsi")
        )
    
    if request.user.is_authenticated:
        return render(request, "table.html", context= {
            "tables" : tables,
        })
    else:
        return redirect("/login")


def tableUpdate(request, id):
    tables = Table.objects.all()
    table_id = Table.objects.get(id=id)
    if request.method == "POST":
        table_id.kota = request.POST.get("kota")
        table_id.ciri_khas = request.POST.get('ciri_khas')
        table_id.provinsi = request.POST.get("provinsi")
        table_id.save()
        return redirect("/table")

    if request.user.is_authenticated:
        return render(request, "table.html", context= {
            "tables" : tables,
            "table_id" : table_id
        })
    else:
        return redirect("/login")
        

def tableDelete(request, id):
    if request.user.is_authenticated:
        table_id = Table.objects.get(id = id)
        table_id.delete()
        return redirect("/table")
    else:
        return redirect("/table")

def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        user = authenticate(request, username = request.POST.get("username"), password = request.POST.get("password"))
        if user is not None:
            auth_login(request, user)
            return redirect("/")
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        u = User.objects.create(
            username = request.POST.get("username")
        )
        u.set_password( request.POST.get("password"))
        u.is_staff = True
        u.is_superuser = True
        u.save()
        auth_login(request, u)
        return redirect("/")
    return render(request, 'register.html')

def keluar(request):
    logout(request)
    return redirect("/")
