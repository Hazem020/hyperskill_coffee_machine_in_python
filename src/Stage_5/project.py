water = 400
milk = 540
coffee = 120
disposable_cups = 9
money = 550


def remaining():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee, "of coffee beans")
    print(disposable_cups, "of disposable cups")
    print("$", money, "of money")


def select_action():
    choice = input("Write action (buy, fill, take, remaining, exit):")
    return choice


def select_drink():
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    return choice


def fill():
    global water, milk, coffee, disposable_cups
    water += int(input("Write how many ml of water do you want to add:"))
    milk += int(input("Write how many ml of milk do you want to add:"))
    coffee += int(input("Write how many grams of coffee beans do you want to add:"))
    disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:"))


def take():
    global money
    print("I gave you $", money)
    money = 0


def check_supply(needed_water, needed_milk, needed_coffee):
    if water < needed_water:
        print('Sorry, not enough water!')
        return False
    if milk < needed_milk:
        print('Sorry, not enough milk!')
        return False
    if coffee < needed_coffee:
        print('Sorry, not enough beans!')
        return False
    if disposable_cups < 1:
        print('Sorry, not enough cups\n')
        return False
    print('I have enough resources, making you a coffee!\n')
    return True


def buy():
    global water, milk, coffee, disposable_cups, money
    drink = select_drink()
    if drink == "back":
        return select_action()
    elif drink == '1':  # espresso
        if check_supply(250, 0, 16):
            water -= 250
            coffee -= 16
            money += 4
            disposable_cups -= 1
    elif drink == '2':  # latte
        if check_supply(350, 75, 20):
            water -= 350
            milk -= 75
            coffee -= 20
            money += 7
            disposable_cups -= 1
    elif drink == '3':  # cappuccino
        if check_supply(200, 100, 12):
            water -= 200
            milk -= 100
            coffee -= 12
            money += 6
            disposable_cups -= 1
    else:
        print('invalid choice')
        return buy()


done = False
while not done:
    action = select_action()
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        remaining()
    elif action == "exit":
        done = True
    else:
        print("invalid choice")
