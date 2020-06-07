from django.urls import path, re_path
from videos import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # The single page
    path('<slug:slug>', views.single, name='video_detail'),
    # The tags page
    path('tags', views.tags, name='video_tags'),
    # The search page
    path('search', views.search, name='video_search'),
]
