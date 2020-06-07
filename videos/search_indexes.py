import datetime
from haystack import indexes
from .models import Video

class VideoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    url = indexes.CharField(model_attr='url')
    embed = indexes.CharField(model_attr='embed')
    title = indexes.CharField(model_attr='title')
    slug = indexes.CharField(model_attr='slug')
    description = indexes.CharField(model_attr='description')
    screenshot = indexes.CharField(model_attr='screenshot')
    trailer = indexes.CharField(model_attr='trailer')
    flipbook = indexes.CharField(model_attr='flipbook')
    actors = indexes.CharField(model_attr='actors')
    tags = indexes.CharField(model_attr='tags')
    mediatype = indexes.CharField(model_attr='mediatype')
    partner = indexes.CharField(model_attr='partner')

    def get_model(self):
        return Video

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
