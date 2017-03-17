from django.conf.urls import url
from . import views

urlpatterns = [
    url('^fullforms/', views.index, name='fullforms'),
]