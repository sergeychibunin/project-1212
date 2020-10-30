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

class Page(models.Model):
    title = models.CharField(max_length=100)


class ContentVideo(models.Model):
    title = models.CharField(max_length=100)
    pages = models.ManyToManyField(Page)


class ContentAudio(models.Model):
    title = models.CharField(max_length=100)
    pages = models.ManyToManyField(Page)
