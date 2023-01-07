from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
coffee_machine_enabled = True
while coffee_machine_enabled:
    user_order = input(f"What would you like? ({machine_menu.get_items()}): ")
    if user_order == "off":
        coffee_machine_enabled = False
    elif user_order == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink_ordered = machine_menu.find_drink(user_order)
        if drink_ordered is not None:
            if coffee_machine.is_resource_sufficient(drink_ordered) and money_machine.make_payment(drink_ordered.cost):
                coffee_machine.make_coffee(drink_ordered)
