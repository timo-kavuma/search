from django.contrib.postgres.search import SearchVector
from haystack.query import SearchQuerySet
from .forms import SearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Video
import random
#from random import shuffle

# Create your views here.
def index(request):
    #categories = ['POV', 'Kissing', 'Booty', 'Hardcore', 'Passion', 'Amatuer', 'Latina', 'Teens', 'College', 'Petite', 'HD', 'Cameltoe']
    #selection = random.choice(categories)
    
    #videos_list = Video.objects.annotate(search=SearchVector(selection),)
    videos_list = Video.objects.annotate(search=SearchVector('title'),).order_by('?')
    #videos_list = Video.objects.all().order_by('?')
        
    paginator = Paginator(videos_list, 80) # 80 posts in each page
    page = request.GET.get('page')
    try:
        vidz = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        vidz = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        vidz = paginator.page(paginator.num_pages)
    return render(request, "videos/index.html", {'page': page, 'videos': vidz})
    #return render(request, "videos/index.html")

def single(request, slug):
    vid = get_object_or_404(Video, slug = slug)
    return render(request, "videos/single.html", {'video': vid})
    #return render(request, "videos/single.html")

def tags(request, tag):
    tags_list = Video.objects.all().filter(tags__icontains=tag)[:150]
    return render(request, "videos/tags.html", {'videos': tags_list})
    #return render(request, "videos/tags.html")

def search(request):
    form = SearchForm()
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(Video).filter(content=cd['query']).load_all()
            
            #count total results
            total_results = results.count()
            
            paginator = Paginator(results, 80) # 80 posts in each page
            page = request.GET.get('page')
            try:
                vidz = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer deliver the first page
                vidz = paginator.page(1)
            except EmptyPage:
                # If page is out of range deliver last page of results
                vidz = paginator.page(paginator.num_pages)
            return render(request,'videos/search.html',{'form': form, 'cd': cd, 'total_results': total_results, 'results': vidz})
            
"""
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Video.objects.annotate(search=SearchVector('title', 'tags'),).filter(search=query)
            
            paginator = Paginator(results, 80) # 80 posts in each page
            page = request.GET.get('page')
            try:
                vidz = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer deliver the first page
                vidz = paginator.page(1)
            except EmptyPage:
                # If page is out of range deliver last page of results
                vidz = paginator.page(paginator.num_pages)
            return render(request,'videos/search.html',{'form': form, 'query': query, 'results': vidz})
"""
