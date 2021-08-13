from rest_framework import serializers
from main.models import Diary, Note

class DiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        fields = ('id', 'title', 'expiration', 'is_private', 'token')

class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note
        fields = ['id', 'text', 'diary']