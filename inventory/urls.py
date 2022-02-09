from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("ingredients/", views.IngredientView.as_view(), name="ingredients"),
    path(
        "ingredients/<pk>/delete/",
        views.DeleteIngredientView.as_view(),
        name="delete_ingredient",
    ),
    path("menu/", views.MenuItemView.as_view(), name="menu"),
    path("purchases/", views.PurchaseView.as_view(), name="purchases"),
]
