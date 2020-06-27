from django.urls import path

from . import views


urlpatterns = [
    path('polls/', views.PollView.as_view(), name='polls'),
    path('polls/<int:pk>/', views.DetailView.as_view(), name='poll_detail'),
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='poll_results'),
    path('polls/<int:question_id>/vote/', views.vote, name='poll_vote'),
]