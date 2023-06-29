from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetalhesView.as_view(), name='detalhes'),
    path('<int:pk>/resultados/', views.ResultadosView.as_view(), name='resultados'),
    path('<int:pk>/votos/', views.VotosView.as_view(), name='votos'),
]