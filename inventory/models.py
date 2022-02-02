from django.db import models


class Ingredient(models.Model):
    """
    Represents an ingredient in the restaurant's inventory
    """

    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=100)
    unit_price = models.FloatField(default=0.00)


class MenuItem(models.Model):
    """
    Represents an item on the restaurant's menu
    """

    title = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0.00)


class RecipeRequirement(models.Model):
    """
    Represents an ingredient and how much of it is required for an item on the restaurant's menu
    """

    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)


class Purchase(models.Model):
    """
    Represents a customer purchase of an item on the restaurant's menu
    """

    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
