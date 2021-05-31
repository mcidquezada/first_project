# Aca vamos a definir  la ruta de la Apps "Blogs"
from django.urls import path     
from . import views
urlpatterns = [
    # path('', views.index),
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),  
    path('blogs/<number>', views.show),
    path('blogs/<number>/edit', views.edit), 
    path('blogs/<number>/delete', views.destroy), 
    # path('blogs/json',views.)
    # path('adios', views.adios),
    # path('saludar/<name>', views.saludar),
    # path('age/<name>/<int:age>', views.age),
]