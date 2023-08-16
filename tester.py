from coffee_menu import Menu
from coffee_maker import CoffeeMaker


menu = Menu()
coffeeMaker = CoffeeMaker()
print("********************************")
print("👋🏼 Welcome to the Coffee Machine!")

while True:
    answer = input("What would you like (espresso/latte/cappuccino)?: ")


    if answer == "off":
        print("👋🏼 See you soon!")
        break
    elif answer == "report":
        coffeeMaker.report()
    elif answer == "refill":
        water = int(input("Refill water: "))
        milk = int(input("Refill milk: "))
        coffee = int(input("Refill coffee: "))
        coffeeMaker.refill(water, milk, coffee)
    elif menu.find_drink(answer) is not None:
        item = menu.find_drink(answer)
        if coffeeMaker.check_resources(item):
            print("Cost of this item: {}".format(item.cost))
            coffeeMaker.make_coffee(item)



    else:
        print("Available drinks: ")
        menu.printMenu()
