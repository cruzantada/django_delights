# from django.shortcuts import render
from .models import Ingredient, MenuItem, Purchase
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView


class HomeView(TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context


class IngredientView(ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"


class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = "/ingredients/"


class MenuItemView(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"


class PurchaseView(ListView):
    model = Purchase
    template_name = "inventory/purchases.html"
