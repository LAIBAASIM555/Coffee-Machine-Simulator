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
    "money": 0.0
}


def print_report():
    print("Water: {}ml".format(resources["water"]))
    print("Milk: {}ml".format(resources["milk"]))
    print("Coffee: {}g".format(resources["coffee"]))
    print("Money: ${:.2f}".format(resources["money"]))


def check_resources(drink):
    for ingredients, amount in MENU[drink]["ingredients"].items():
        if resources[ingredients] < amount:
            return False
        return True


def process_coin():
    print("Insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def make_coffee(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    resources["money"] += MENU[drink]["cost"]
    print("Here is your {}. Enjoy!☕".format(drink))


while True:
    customer = input("What would you like? (espresso/latte/cappuccino): ")
    if customer == "off":
        break
    elif customer == "report":
        print_report()
    elif customer in MENU:
        if check_resources(customer):
            total = process_coin()
            if total >= MENU[customer]["cost"]:
                if total > MENU[customer]["cost"]:
                    print("Here is ${:.2f} in change.".format(total - MENU[customer]["cost"]))
                make_coffee(customer)
            else:
                print("Sorry, that's not enough money😢. Money refunded.")
    else:
        print("Invalid input. Please try again.")














