class TeaMaker:
    """Models the machine that makes the tea"""
    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 500,
            "tea_leaves": 200,
            "sugar": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"tea_leaves: {self.resources['tea_leaves']}g")
        print(f"sugar: {self.resources['sugar']}tsp")

    def refill(self):
        for key in self.resources:
            self.resources[key] += 100
        print("Machine refilled successfully!")
        self.report()
    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_tea(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
