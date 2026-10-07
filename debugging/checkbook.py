#!/usr/bin/python3
import math


class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if not math.isfinite(amount) or amount <= 0:
            print("Invalid amount. Please enter a positive finite number.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if not math.isfinite(amount) or amount <= 0:
            print("Invalid amount. Please enter a positive finite number.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()
    while True:
        try:
            action = input(
                "What would you like to do? "
                "(deposit, withdraw, balance, exit): "
            ).strip().lower()

            if action == 'exit':
                break
            elif action == 'deposit':
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            elif action == 'withdraw':
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            elif action == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a numeric amount.")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
