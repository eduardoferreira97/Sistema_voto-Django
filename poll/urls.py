from django.urls import path

from . import views

app_name = 'poll'
urlpatterns = [
    # /poll/
    path('', views.index, name='index'),
    # ex: /poll/3/
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /poll/3/results/
    path('<int:question_id>/results/',views.results,name='results'),
    # ex: /poll/3/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]