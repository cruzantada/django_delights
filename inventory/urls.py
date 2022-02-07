from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("account/", include("django.contrib.auth.urls"), name="login"),
    path("ingredient/list", views.IngredientList.as_view(), name="ingredientlist"),
    path(
        "ingredient/delete/<pk>",
        views.IngredientDelete.as_view(),
        name="ingredientdelete",
    ),
    path("menuitem/list", views.MenuItemList.as_view(), name="menuitemlist"),
    path("purchase/list", views.PurchaseList.as_view(), name="purchaselist"),
]
