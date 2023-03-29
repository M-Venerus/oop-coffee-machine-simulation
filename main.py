from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = MenuItem("espresso", 50, 0, 18, 1.50)
latte = MenuItem("latte", 200, 150, 24, 2.50)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.00)
menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
    
    
def drink_choice():
    """Prompt user for drink selection. Secret value 'report' generates resource levels."""
    user_drink = input(f"What beverage would you like? ({menu.get_items()}): ")
    if user_drink == "report":
        coffeemaker.report()
        moneymachine.report()
        return "reset"
    else:
        return menu.find_drink(user_drink)
    

def check_resources(drink):
    """Check if resources are available for selected drink."""
    if coffeemaker.is_resource_sufficient(drink):
        pass
    else:
        main()
            

def drink_price(drink):
    """Return price of selected drink."""
    cost = drink.cost
    cost_formatted = "{:.2f}".format(cost)
    print(f"A {drink.name} costs $ {cost_formatted}")
    return cost
        

def main():
    """Execute coffee machine simulation."""
    drink = drink_choice()
    if drink == "reset":
        main()
    else:
        check_resources(drink)
        price = drink_price(drink)
        if moneymachine.make_payment(price):
            pass
        else:
            main()
        coffeemaker.make_coffee(drink)
        main()


main()

