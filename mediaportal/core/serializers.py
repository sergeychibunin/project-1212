from rest_framework import serializers
from core.models import Page, ContentAudio, ContentText, ContentVideo


class PageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='page-detail', read_only=True)

    class Meta:
        model = Page
        fields = ['id', 'url']


class ContentTextDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentText
        fields = ['title', 'body']


class ContentAudioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentAudio
        fields = ['title', 'audio_url', 'rate']


class ContentVideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentVideo
        fields = ['title', 'video_url', 'subtitles_url']


class PageDetailSerializer(serializers.ModelSerializer):
    texts = ContentTextDetailSerializer(many=True, read_only=True)
    audios = ContentAudioDetailSerializer(many=True, read_only=True)
    videos = ContentVideoDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['id', 'title', 'texts', 'audios', 'videos']
