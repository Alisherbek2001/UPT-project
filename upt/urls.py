from django.urls import path
from .views import *


urlpatterns = [
    path('',HomePageAPIView.as_view(),name='home-page'),
    path('projects/',ProjectPageAPIView.as_view(),name='projects-page'),
    path('about/',MemberAPIView.as_view(),name='member-page')
]