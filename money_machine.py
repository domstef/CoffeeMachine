
class MoneyMachine:

    coins = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        """ Makes a money report """
        print("* Money: ${}".format(self.profit))

    def insert_coins(self):
        """ Method to get coins from the user. It handles the ValueError if there is a mistake in input type."""

        print("Please insert coins.")
        try:
            quarters = int(input("Insert quarters ($0.25): "))
            dimes = int(input("Insert dimes ($0.1): "))
            nickles = int(input("Insert nickles ($0.05): "))
            pennies = int(input("Insert pennies ($0.01): "))
        except ValueError:
            quarters, dimes, nickles, pennies = 0, 0, 0, 0
            self.insert_coins()


        total = self.coins["quarters"] * quarters + self.coins["dimes"] * dimes + self.coins["nickles"] * nickles + self.coins[
            "pennies"] * pennies

        return total

    def process_coins(self, coffee):
        """
        Method checks if the given money is sufficient to make a payment for specific coffee. If so, it gives a rest
        in change.
        """

        total = self.insert_coins()
        enough_coins = True

        if total < coffee.cost:
            print("Sorry, you need to give more money.")
            enough_coins = False
        else:
            print("You've inserted ${:.2f}.".format(total))
            self.profit += coffee.cost
            print("Here's ${:.2f} in change.".format(total - coffee.cost))
        return enough_coins
