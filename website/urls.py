from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:code>', views.PlayCadavreView.as_view(), name='cadavre_detail'),
    path('<slug:code>/send_cadavre', views.send_cadavre, name='send_cadavre'),
]