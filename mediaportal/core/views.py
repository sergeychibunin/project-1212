from django.shortcuts import render
from rest_framework import generics
from core.models import Page
from core.serializers import PageSerializer, \
    PageDetailSerializer


class PageListView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageDetailView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageDetailSerializer
