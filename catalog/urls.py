from django.urls import path, include
from . import views

urlpatterns = [
    # path('catalog/', include('catalog.urls')),
    path('', views.index, name='index'),


]
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]
