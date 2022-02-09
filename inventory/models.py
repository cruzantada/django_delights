from django.db import models


class Ingredient(models.Model):
    """
    Represents an ingredient in the restaurant's inventory
    """

    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=100)
    unit_price = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/ingredients"

    def __str__(self):
        return f"""
        name = {self.name},
        quantity = {self.quantity},
        unit = {self.unit},
        unit price = {self.unit_price}
        """


class MenuItem(models.Model):
    """
    Represents an item on the restaurant's menu
    """

    title = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/menu"

    def __str__(self):
        return f"title = {self.title}, price = {self.price}"


class RecipeRequirement(models.Model):
    """
    Represents an ingredient and how much of it is required for an item on the restaurant's menu
    """

    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def get_absolute_url(self):
        return "/menu"

    def __str__(self):
        return f"""
        menu item = {self.menu_item.__str__()},
        ingredient = {self.ingredient.name},
        quantity = {self.quantity}
        """


class Purchase(models.Model):
    """
    Represents a customer purchase of an item on the restaurant's menu
    """

    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/purchases"

    def __str__(self):
        return f"menu item = {self.menu_item.__str__()}, time = {self.timestamp}"
