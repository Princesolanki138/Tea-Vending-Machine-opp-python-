class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, tea_leaves,sugar, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "tea_leaves": tea_leaves,
            "sugar":sugar
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem("green_tea", water=200, milk=0, tea_leaves=2,sugar = 0,cost=40),
            MenuItem("black_tea", water=240, milk=0, tea_leaves=2,sugar = 0,cost=20),
            MenuItem("milk_tea", water=100, milk=140, tea_leaves=3,sugar = 0,cost=15)
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
