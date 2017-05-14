from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect

from elasticsearch import Elasticsearch

es = Elasticsearch(['http://ec2-34-207-133-220.compute-1.amazonaws.com:9200/'])

def index(request):
    query = {
        "query" : {
            "match_all" : {}
        }
    }
    res = es.search(index="tweet-good", body=query)
    tw = res['hits']['hits']
    tn = []
    
    for t in tw:
      tn.append(t['_source'])
      print t
      print "Entro"
    return render_to_response('index.html',{'tweets':tn})

def visualize(request):
    return render_to_response('visualize.html')

def crowdfunding_detail(request):
    return render_to_response('crowdfunding_detail.html')

def crowdfunding_listing(request):
    return render_to_response('crowdfunding_listing.html')

def ranking_listing(request):
    return render_to_response('ranking_listing.html')

def challenge_detail(request):
    return render_to_response('challenge_detail.html')

def challenge_listing_list(request):
    return render_to_response('challenge_listing_list.html')


def admin_index(request):
    return render_to_response('AdminIndex.html')