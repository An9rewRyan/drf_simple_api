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
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets


class DiaryList(generics.ListCreateAPIView):

    def post(self, request, format=None):

        serializer = DiarySerializer(data=request.data)

        if serializer.is_valid():

            if serializer.validated_data['is_private'] == False:

                del serializer.validated_data['expiration']
            
            print(serializer.validated_data)


            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer

class DiaryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Diary.objects.all()
    serializer_class = DiarySerializer

# class NoteList(generics.ListCreateAPIView):

#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

# class NoteDetail(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

# class DiaryList(APIView):

    

#     def get(self, request, format=None):
#         diaries = Diary.objects.all()
#         serializer = DiarySerializer(diaries, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
        
#         serializer = DiarySerializer(data=request.data)
#         print(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DiaryDetail(APIView):

#     def get_diary(self, diary_id):
#         try:
#             return Diary.objects.get(pk=diary_id)
#         except Diary.DoesNotExist:
#             raise Http404

#     def get(self, request, diary_id, format=None):
#         diary = self.get_diary(diary_id)
#         serializer = DiarySerializer(diary)
#         return Response(serializer.data)

#     def put(self, request, diary_id, format=None):
#         diary = self.get_diary(diary_id)
#         serializer = DiarySerializer(diary, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, diary_id, format=None):
#         note = self.get_diary(diary_id)
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class NoteList(APIView):

#     def get_diary(self, diary_id):
#         try:
#             return Diary.objects.get(pk=diary_id)
#         except Diary.DoesNotExist:
#             raise Http404
    
#     def get_notes(self, note_id, diary_id):
#         try:
#             return Note.objects.filter(diary_id = diary_id)
#         except Note.DoesNotExist:
#             raise Http404
    
#     def get(self, request, diary_id, format=None):
#         notes = Note.objects.filter(diary_id=diary_id)
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)

#     def post(self, request, diary_id, format=None):

#         serializer = NoteSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteList(generics.ListCreateAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_diary(self, diary_id):
        try:
            return Diary.objects.get(pk=diary_id)
        except Diary.DoesNotExist:
            raise Http404
    
    def get_notes(self, note_id, diary_id):
        try:
            return Note.objects.filter(diary_id = diary_id)
        except Note.DoesNotExist:
            raise Http404
    
    def list(self, request, diary_id, format=None):
        notes = Note.objects.filter(diary_id=diary_id)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def create(self, request, diary_id, format=None):

        serializer = NoteSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_diary(self, diary_id):
        try:
            return Diary.objects.get(token=diary_id)
        except Diary.DoesNotExist:
            raise Http404
    
    def get_note(self, note_id, diary_id):
        try:
            return Note.objects.get(pk=note_id, diary_id = diary_id)
        except Note.DoesNotExist:
            raise Http404

    def retrieve(self, request, note_id, diary_id, format=None):
        note = self.get_note(note_id, diary_id)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def update(self, request, note_id, diary_id, format=None):
        note = self.get_note(note_id, diary_id)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, note_id,diary_id, format=None):
        note = self.get_note(note_id, diary_id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)