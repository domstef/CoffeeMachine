from money_machine import MoneyMachine


class CoffeeMaker:
    """
    Creates a process of making coffee.
    """

    def __init__(self):
        self.resources = {"water": 300,
                          "milk": 200,
                          "coffee": 100
                          }
        self.moneyMachine = MoneyMachine()


    def report(self):
        """ Report the status of the Coffee Machine. """

        print("---- Current resources of the coffee machine ----")
        print("* Water: {}ml".format(self.resources["water"]))
        print("* Milk: {}ml".format(self.resources["milk"]))
        print("* Coffee: {}g".format(self.resources["coffee"]))


    def refill(self, water=300, milk=200, coffee=100):
        """ Refills the resources of the Coffee Machine """
        self.resources["water"] += water
        self.resources["milk"] += milk
        self.resources["coffee"] += coffee



    def check_resources(self, coffee):
        """
        Checks the resources and returns if the resources are enough to make specific coffee
        """

        enough_resources = True
        for key in self.resources:
            if self.resources[key] - coffee.ingredients[key] < 0:
                enough_resources = False
                print("We're sorry, there is not enough {} 😥".format(key))
        return enough_resources


    def make_coffee(self, coffee):
        """
        Method checks the resources to make a coffee, then proceeds the payment and if its successful - makes a coffee.
        :param coffee: name of a coffee to make
        """

        if self.check_resources(coffee):
            if self.moneyMachine.process_coins(coffee):
                print("Enjoy your {}! Have a nice day! ☕".format(coffee.name))
                self.resources = {key: self.resources[key] - coffee.ingredients[key] for key in self.resources}
