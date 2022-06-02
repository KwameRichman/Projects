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
}

logo = """

  |  / \ \      /  \     \  |  __| )  __|     __|   _ \  __| __| __|  __|    |  |   _ \  |  |   __|  __| 
  . <   \ \ \  /  _ \   |\/ |  _| / \__ \    (     (   | _|  _|  _|   _|     __ |  (   | |  | \__ \  _|  
 _|\_\   \_/\_/ _/  _\ _|  _| ___|  ____/   \___| \___/ _|  _|  ___| ___|   _| _| \___/ \__/  ____/ ___| 
                                                                                                         
"""

# TODO 3: Print report.
def report_statement():
    """Formats information for the coffee resources report"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"


# TODO 4: Check if resources are sufficient
def is_resource_sufficient(drink_ingredients):
    """Returns True when ingredients are sufficient or False when insufficient.
    Also deducts used resources"""
    is_enough = True
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
        # TODO 7: Make Coffee.
        else:
            resources[item] -= drink_ingredients[item]
    return is_enough


# TODO 5: Process coins.
def process_coins():
    """Take coins, converts to dollars and returns total"""
    print("Please insert coins.")
    quarter = float(input("How many quarters?: ")) * 0.25
    dime = float(input("How many dimes?: ")) * 0.10
    nickle = float(input("How many nickles?: ")) * 0.05
    penny = float(input("How many pennies?: ")) * 0.01
    total_cash = round(quarter + dime + nickle + penny, 2)
    return total_cash


# TODO 6: Check transaction successful?
def is_transaction_successful(money_received, cost):
    """Returns True if the money is enough or more and finds change or
    false if the money is not enough"""
    if money_received > cost:
        change = money_received - cost
        print(f"Here is ${change} in change.")
        return True
    elif money_received == cost:
        return True
    else:
        print("Insufficient funds. Here is a refund.")
        return False


print(logo)
money = 0
turn_off_coffee = False

while not turn_off_coffee:
    # TODO 1: Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt.
    if choice == 'off':
        print("Shutting down....")
        turn_off_coffee = True

    elif choice == 'report':
        print(report_statement())

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            user_money = process_coins()
            if is_transaction_successful(user_money, drink["cost"]):
                money += drink["cost"]
                print(f"Here is your {choice}. Enjoy!")
