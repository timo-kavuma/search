from django.shortcuts import render
from videos.models import Video

# Create your views here.
def index(request):
    #videos_list = Video.objects.all()
    #return render(request, "videos/index.html", {'posts': videos_list})
    return render(request, "videos/index.html")

def single(request, slug):
    #post = get_object_or_404(Video, slug = slug)
    #return render(request, "videos/single.html", {'post': post})
    return render(request, "videos/single.html")

def tags(request):
    #tags_list = Video.objects.all()
    #return render(request, "videos/tags.html", {'posts': tags_list})
    return render(request, "videos/tags.html")

def search(request):
    #search_list = Video.objects.all()
    #return render(request, "videos/search.html", {'posts': search_list})
    return render(request, "videos/search.html")

