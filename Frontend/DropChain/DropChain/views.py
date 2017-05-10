from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect


def index(request):
    return render_to_response('index.html')

def crowdfunding_detail(request):
    return render_to_response('crowdfunding_detail.html')

def crowdfunding_listing(request):
    return render_to_response('crowdfunding_listing.html')