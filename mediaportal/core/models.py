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
    subtitles_url = models.URLField()
    counter = models.PositiveIntegerField()


class ContentAudio(models.Model):
    title = models.CharField(max_length=100)
    rate = models.IntegerField()
    counter = models.PositiveIntegerField()


class ContentText(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    counter = models.PositiveIntegerField()


class Page(models.Model):
    title = models.CharField(max_length=100)
    videos = models.ManyToManyField(ContentVideo)
    audios = models.ManyToManyField(ContentAudio)
    texts = models.ManyToManyField(ContentText)
