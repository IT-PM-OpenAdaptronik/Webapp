from django.urls import path

from . import views

app_name='profile'
urlpatterns = [
    path('profile', views.show_me, name='index')
    #hier Name der Funktion in views
    # für anderen User  name =<slug:token>
    ]
