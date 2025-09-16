from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import PlaceForm
import random

def index(request):
    if "places" not in request.session:
        request.session["places"] = [
            {
                "id": 1,
                "title": "Тісто та хміль",
                "description": "Смачна італійська кухня з європейським нахилом.",
                "place_type": "Ресторан",
                "location": "Метро Дарниця",
                "rating": 4.5,
                "created_at": "2025-09-16"
            },
            {
                "id": 2,
                "title": "Нац. бот. сад ім. Гришка",
                "description": "Просторі схили Печерську, затишні кущі для лежання.",
                "place_type": "Парк",
                "location": "Метро Звіриницька",
                "rating": 4.0,
                "created_at": "2025-09-16"
            },
            {
                "id": 3,
                "title": "Мама Манана",
                "description": "Прекрасна грузинська кухня, вааах смачно!",
                "place_type": "Ресторан",
                "location": "Багато закладів по Києву",
                "rating": 5.0,
                "created_at": "2025-09-16"
            },
            {
                "id": 4,
                "title": "Pan Chang",
                "description": "Азійська кухня, смачно, доволі гучна музика у залі.",
                "place_type": "Ресторан",
                "location": "Поділ",
                "rating": 4.0,
                "created_at": "2025-09-16"
            },
            {
                "id": 5,
                "title": "Гамбургерна NUNU",
                "description": "Одні з найкращих бургерів у Києві! Дуже стильний інтер'єр.",
                "place_type": "Ресторан",
                "location": "Поділ",
                "rating": 4.0,
                "created_at": "2025-09-16"
            },
        ]

    chosen_place = None
    if request.method == "POST":
        places = request.session.get("places", [])
        if places:
            weights = [p['rating'] for p in places]
            chosen_place = random.choices(places, weights=weights, k=1)[0]

    return render(request, "places_to_go/index.html", {"chosen_place": chosen_place})


def places_list(request):
    places = request.session.get("places", [])
    return render(request, "places_to_go/places_list.html", {"places": places})

def place_detail(request, pk):
    places = request.session.get("places", [])
    place = next((p for p in places if p['id'] == pk), None)
    if not place:
        return redirect("places_list")
    return render(request, "places_to_go/place_detail.html", {"place": place})

def add_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            places = request.session.get("places", [])
            new_id = len(places) + 1
            new_place = {
                "id": new_id,
                "title": form.cleaned_data["title"],
                "description": form.cleaned_data["description"],
                "place_type": form.cleaned_data["place_type"],
                "location": form.cleaned_data["location"],
                "rating": float(form.cleaned_data["rating"]),
                "created_at": "2025-09-16",
            }
            places.append(new_place)
            request.session["places"] = places
            return redirect("places_list")
    else:
        form = PlaceForm()
    return render(request, "places_to_go/add_place.html", {"form": form})
