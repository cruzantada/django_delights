from django.shortcuts import render
from .models import Ingredient, MenuItem, Purchase
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import DeleteView


@login_required
def home(request):
    context = {"name": request.user}
    return render(request, "inventory/home.html", context)


class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"


class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"


class MenuItemList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu_item_list.html"


class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
