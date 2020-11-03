from django.shortcuts import render
from rest_framework import generics
from core.models import Page
from core.serializers import PageSerializer, \
    PageDetailSerializer
from core.tasks import increase_counter as celery_increase_counter


class PageListView(generics.ListAPIView):
    queryset = Page.objects.all().order_by('id')
    serializer_class = PageSerializer


class PageDetailView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageDetailSerializer

    def get(self, request, *args, **kwargs):
        response = self.retrieve(request, *args, **kwargs)
        
        instance = self.get_object()
        for text in instance.texts.all():
            celery_increase_counter.delay(text.id, text.__class__.__name__)
        for audio in instance.audios.all():
            celery_increase_counter.delay(audio.id, audio.__class__.__name__)
        for video in instance.videos.all():
            celery_increase_counter.delay(video.id, video.__class__.__name__)

        return response
