from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.places_list, name="places_list"),
    path("place/<int:pk>/", views.place_detail, name="place_detail"),
    path("add_place/", views.add_place, name="add_place"),
]
