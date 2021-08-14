from rest_framework import serializers
from main.models import Diary, Note
class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['id', 'text', 'diary_id']

class DiarySerializer(serializers.ModelSerializer):
    notes = serializers.StringRelatedField(many=True)
    class Meta:
        model = Diary
        fields = ('id', 'title', 'expiration', 'is_private', 'notes')

