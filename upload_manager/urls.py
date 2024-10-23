from django.urls import path
from . import views

urlpatterns = [
  path(route='upload/', view=views.UploadView.as_view()),
]