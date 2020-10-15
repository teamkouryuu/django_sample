from django.urls import path 
from . import views

app_name = "polls"
urlpatterns = [
    # path関数の引数[route],[view],[kwargs],[name]

    
    # ex: /polls/
    path('', views.indexView.as_view(), name='index'),

    # ex: /polls/<int>
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # ex: /polls/<int>/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/<int>/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

]