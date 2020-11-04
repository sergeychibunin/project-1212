from django.db import models
from sortedm2m.fields import SortedManyToManyField

"""
There is a primitive scheme.

Page
--
id
title

ContentVideo
--
id
title

PageContentVideo
--
id
page_id
content_video_id

ContentAudio
--
id
title

ContentText
--
id
title
"""

class ContentMixin:
    def increase_counter(self):
        assert isinstance(self, models.Model)
        assert hasattr(self, 'counter')
        self.counter += 1
        self.save()


class ContentVideo(models.Model, ContentMixin):
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    subtitles_url = models.URLField(null=True, blank=True)
    counter = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class ContentAudio(models.Model, ContentMixin):
    title = models.CharField(max_length=100)
    audio_url = models.URLField()
    rate = models.IntegerField()
    counter = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class ContentText(models.Model, ContentMixin):
    title = models.CharField(max_length=100)
    body = models.TextField()
    counter = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=100)
    videos = SortedManyToManyField(ContentVideo, blank=True)
    audios = SortedManyToManyField(ContentAudio, blank=True)
    texts = SortedManyToManyField(ContentText, blank=True)

    def __str__(self):
        return self.title
