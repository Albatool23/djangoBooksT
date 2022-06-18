

from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index),
    re_path(r'^book/$',views.book),
   # re_path(r'^book/addAuthortobook/$',views.book),
     path('author',views.authors),
    re_path(r'^showAuthor/$',views.showAuthor),


]