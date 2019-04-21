
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views, api_views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

 # API views
 #    url(r'^api/questions/$', api_views.QuestionList.as_view()),
 #    url(r'^api/questions/(?P&lt;pk&gt;[0-9]+)/$', api_views.QuestionDetail.as_view()),
 #    url(r'^api/choices/(?P&lt;pk&gt;[0-9]+)/$', api_views.ChoiceDetail.as_view()),
    path('api/questions/$', api_views.QuestionList.as_view(), name='get_create'),
    path('api/questions/(?P&lt;pk&gt;[0-9]+)/$', api_views.QuestionDetail.as_view(), name='get_delete'),
    path('api/choices/(?P&lt;pk&gt;[0-9]+)/$', api_views.ChoiceDetail.as_view(), name='get_choice'),

]
