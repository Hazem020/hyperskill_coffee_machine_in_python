water_available = int(input("Write how many ml of water the coffee machine has:"))
milk_available = int(input("Write how many ml of milk the coffee machine has:"))
coffee_available = int(input("Write how many grams of coffee beans the coffee machine has:"))
cups = int(input("Write how many cups of coffee you will need:"))
water = water_available // 200
milk = milk_available // 50
coffee = coffee_available // 15
cups_possible = min(water, milk, coffee)
if cups_possible > cups:
    print(f"Yes, I can make that amount of coffee (and even {(cups_possible - cups)} more than that)")
elif cups_possible == cups:
    print("Yes, I can make that amount of coffee")
else:
    print(f"No, I can make only {cups_possible} cup(s) of coffee")
