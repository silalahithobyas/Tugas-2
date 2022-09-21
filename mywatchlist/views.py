from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_watchlist = MyWatchListItem.objects.all()
    
    count = 0
    elses = 0
    success = ""

    for data in data_watchlist:
        if data.watched == "Yes":
            count = count + 1
        else:
            elses = elses + 1

    if count > elses:
        success = "Selamat, kamu sudah banyak menonton!"
    else:
        success = "Wah, kamu masih sedikit menonton!"

    context = {
        'nama': 'Thobyas Muda Parlindungan',
        'studentid' : '2106650001',
        'watchedTrue': count,
        'watchedFalse': elses,
        'watchedMany': success
    }
    return render(request, "home.html", context)

def show_html(request):
    data_watchlist = MyWatchListItem.objects.all()
    context = {
        'list_barang': data_watchlist,
        'nama': 'Thobyas Muda Parlindungan'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
