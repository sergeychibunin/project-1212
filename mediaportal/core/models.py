from django.db import models

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

class ContentVideo(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    subtitles_url = models.URLField(null=True, blank=True)
    counter = models.PositiveIntegerField()


class ContentAudio(models.Model):
    title = models.CharField(max_length=100)
    audio_url = models.URLField()
    rate = models.IntegerField()
    counter = models.PositiveIntegerField()


class ContentText(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    counter = models.PositiveIntegerField()


class Page(models.Model):
    title = models.CharField(max_length=100)
    videos = models.ManyToManyField(ContentVideo, blank=True)
    audios = models.ManyToManyField(ContentAudio, blank=True)
    texts = models.ManyToManyField(ContentText, blank=True)
