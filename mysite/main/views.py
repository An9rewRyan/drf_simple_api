from datetime import date
from main.models import Diary, Note
from main.serializers import DiarySerializer, NoteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'diaries': reverse('diaries-list', request=request, format=format),
        'notes': reverse('notes-list', request=request, format=format)
    })

class DiaryList(APIView):
    
    def get(self, request, format=None):
        diaries = Diary.objects.all()
        serializer = DiarySerializer(diaries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DiarySerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiaryDetail(APIView):
    """
    Извлекает, обновляет или удаляет экземпляр сниппета.
    """
    def get_diary(self, diary_id):
        try:
            return Diary.objects.get(pk=diary_id)
        except Diary.DoesNotExist:
            raise Http404

    def get(self, request, diary_id, format=None):
        diary = self.get_diary(diary_id)
        serializer = DiarySerializer(diary)
        return Response(serializer.data)

    def put(self, request, diary_id, format=None):
        diary = self.get_diary(diary_id)
        serializer = DiarySerializer(diary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, diary_id, format=None):
        note = self.get_diary(diary_id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NoteList(APIView):

    def get_diary(self, diary_id):
        try:
            return Diary.objects.get(pk=diary_id)
        except Diary.DoesNotExist:
            raise Http404
    
    def get_notes(self, note_id, diary_id):
        try:
            return Note.objects.filter(diary = diary_id)
        except Note.DoesNotExist:
            raise Http404
    
    def get(self, request, diary_id, format=None):
        notes = Note.objects.filter(diary=diary_id)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request, diary_id, format=None):
        data = dict(request.data)
        #values = list(request.values())
        #print(data)
        diary = Diary.objects.get(pk=diary_id)
        data.update({'diary':diary.token})
        serializer = NoteSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetail(APIView):
    """
    Извлекает, обновляет или удаляет экземпляр сниппета.
    """
    # def get_diary(self, diary_id):
    #     try:
    #         return Diary.objects.get(token=diary_id)
    #     except Diary.DoesNotExist:
    #         raise Http404
    
    def get_note(self, note_id, diary_id):
        try:
            return Note.objects.get(pk=note_id, diary = diary_id)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, note_id, diary_id, format=None):
        note = self.get_note(note_id, diary_id)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, note_id, diary_id, format=None):
        note = self.get_note(note_id, diary_id)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, note_id,diary_id, format=None):
        note = self.get_note(note_id, diary_id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)