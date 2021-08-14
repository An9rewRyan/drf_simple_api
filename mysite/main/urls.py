from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from main import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from main import views

# Create a router and register our viewsets with it.



urlpatterns = [
    path('diaries/', views.DiaryList.as_view(), name = 'diaries-list'),
    path('diaries/<int:pk>/', views.DiaryDetail.as_view(), name = 'diary-detail'),
    path('notes/<int:diary_id>/', views.NoteList.as_view(), name = 'notes-list'),
    path('notes/<int:diary_id>/<int:note_id>/', views.NoteDetail.as_view(), name = 'notes-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)