from django.urls import path

from . import views

urlpatterns = [
    path(route='',          view=views.index,       name='index'),
    path(route="base_page/",view=views.base_page,   name="base_page"),
]