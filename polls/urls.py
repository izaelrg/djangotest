from django.urls import path

from . import views


urlpatterns = [
    path('polls/', views.polls, name='polls'),
    path('polls/<int:question_id>/', views.detail, name='poll_detail'),
    path('polls/<int:question_id>/results/', views.results, name='poll_results'),
    path('polls/<int:question_id>/vote/', views.vote, name='poll_vote'),
]
