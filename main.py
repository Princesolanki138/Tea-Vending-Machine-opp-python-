from menu import Menu
from tea_maker import TeaMaker
from money_machine import MoneyMachine
import getpass
class MakeTea:
    def __init__(self):
        self.is_on = True
        self.TeaMaker = TeaMaker()
        self.moneyMachine = MoneyMachine()
        self.menu = Menu()
        self.options = self.menu.get_items()
    
    def start(self):

        while self.is_on:
            choice = input(f"What would you like?: {self.options} :").lower() 
            if choice == "off":
                self.is_on = False
            elif choice == "report":
                self.TeaMaker.report()       
                self.moneyMachine.report()
            elif choice == "refill":
                self.TeaMaker.refill()
            elif choice == "reset profit":
                password = getpass.getpass("Enter admin password to reset profit: ")
                if password == "Admin123":
                    self.moneyMachine.reset_profit()
                else:
                    print("Incorrect Password access denied")    
            else:
                drink = self.menu.find_drink(choice)
                wants_sugar = int(input("How much sugar do you need :(if No then type 0 else type number of tsp): ")or 0)  
                drink.ingredients["sugar"] = wants_sugar
                if drink:
                    if self.TeaMaker.is_resource_sufficient(drink):
                        if self.moneyMachine.make_payment(drink.cost):
                            self.TeaMaker.make_tea(drink)
                else:
                    print("Invalid selection. Please choose a valid item.")            
                
machine = MakeTea()
machine.start()

