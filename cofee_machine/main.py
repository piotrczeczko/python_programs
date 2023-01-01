MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def print_report():
    """Check/show what is the status of machine resources."""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def check_resources(ingredients):
    """Check if there is enough resources to create this type of coffee."""
    enough_resources_to_process = True
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            #enough_resources_to_process = False
            return False
    return True #enough_resources_to_process


def process_coins():
    print("Please insert coins.")
    total_amount = int(input("How many quarters?: ")) * 0.25
    total_amount += int(input("How many dimes?: ")) * 0.1
    total_amount += int(input("How many nickles?: ")) * 0.05
    total_amount += int(input("How many pennies?: ")) * 0.01
    return total_amount


def verify_transaction(user_money, coffee_name):
    """Check if user inserted enough money"""
    if user_money < MENU[coffee_name]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif user_money > MENU[coffee_name]["cost"]:
        user_change = round(user_money - MENU[coffee_name]["cost"],2)
        print(f"Here is ${user_change} in change.")

    resources["money"] += MENU[coffee_name]["cost"]
    return True


def make_coffee(coffee_name):
    # print_report()
    # deduct resources
    for resource in MENU[coffee_name]["ingredients"]:
        resources[resource] -= MENU[coffee_name]["ingredients"][resource]
    # print_report()
    print(f"Here is your {coffee_name} ☕ Enjoy!")


coffee_machine_enabled = True
while coffee_machine_enabled:
    user_transaction = False
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    if user_order == "off":
        coffee_machine_enabled = False
    elif user_order == "report":
        print_report()
    elif user_order in MENU:
        enough_resources = check_resources(MENU[user_order]["ingredients"])
        if enough_resources:
            user_inserted_money = process_coins()
            user_transaction_successful = verify_transaction(user_inserted_money, user_order)
            if user_transaction_successful:
                make_coffee(user_order)





