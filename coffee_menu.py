

class Coffee:
    """
    This class creates each coffee in the menu.
    """

    def __init__(self, name, water, milk, coffee, cost):
        """
        Creating coffee and declaring its attributes.
        :param name: Name of the drink
        :param water: Water needed to make drink [ml]
        :param milk: Milk needed to make drink [ml]
        :param coffee: Coffee needed to make drink [g]
        :param cost: Cost of the coffee [$]
        """
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


    def printCoffee(self):
        """
        Printing all information about a drink
        """
        print("{}: {}ml of  water, {}ml of milk and {}g of coffee. ${}".format(self.name,
                                                                               self.ingredients["water"],
                                                                               self.ingredients["milk"],
                                                                               self.ingredients["coffee"], self.cost))


class Menu:
    """
    This class models a menu in the Coffee Machine
    """

    def __init__(self):
        """
        Creates a list of drinks in the Menu by creating objects of Coffee class.
        """

        self.menu = [
            Coffee(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            Coffee(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            Coffee(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0)
        ]

    def printMenu(self):
        """
        Printing actual menu.
        """

        print("------ MENU ----- ")
        for item in self.menu:
            item.printCoffee()

    def addCoffee(self, name, water, milk, coffee, cost):
        """
        Adding coffee by the user.
        :param name: Name of the coffee
        :param name: Name of the drink
        :param water: Water needed to make drink [ml]
        :param milk: Milk needed to make drink [ml]
        :param coffee: Coffee needed to make drink [g]
        :param cost: Cost of the coffee [$]
        """

        print("Adding coffee to the menu...")
        self.menu.append(Coffee(name, water, milk, coffee, cost))

    def find_drink(self, name):
        """
        Finding drink by name in the actual menu.
        :param name:  Name of the drink
        :return: if the drink is available in the menu
        """

        for item in self.menu:
            if name == item.name:
                return item
        print("The drink is not available! Sorry!")
        return None

    def getDrink(self, name):

        if self.find_drink(name) is not None:
            return self.find_drink(name)
        else:
            print("Choose drinks from the menu!")
            self.printMenu()
