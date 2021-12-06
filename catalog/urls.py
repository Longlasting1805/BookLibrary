from django.urls import path, include
from . import views

urlpatterns = [
    # path('catalog/', include('catalog.urls')),
    path('', views.index, name='index'),

]
