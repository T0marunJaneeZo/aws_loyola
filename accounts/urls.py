from django.urls import path
from .views import student_batch_create_view

urlpatterns = [
    path('student-batch/', student_batch_create_view, name='student_batch_create'),
]
