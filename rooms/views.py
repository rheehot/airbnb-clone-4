from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models, forms


# Create your views here.
class HomeView(ListView):
    """ Homeview Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomView(DetailView):
    """ RoomView Definition """

    model = models.Room


def search(request):
    form = forms.SearchForm()
    return render(request, "rooms/search.html", {"form": form})
