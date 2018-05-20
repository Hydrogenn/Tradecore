from django.urls import path

from . import views


#TODO add view/edit pages for each factory
#TODO add factory overview page
#TODO add new factory page
app_name = 'tradecore'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
]