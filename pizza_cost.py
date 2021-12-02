#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: DEC. 1, 2021
# This program calculates the cost of buying
# a pizza with a user inputted diameter


import constant


def main():
    # This function asks for the radius and then calculates the cost
    print("This program calculates the cost of a pizza by it's diameter.")
    # Input
    diameter = int(input("Enter diameter of your pizza: "))

    # Process
    total = (2 + 2.25 + (1.5 * diameter))
    tax = constant.HST * total
    final_cost = total + tax

    # Output
    print(" ")
    print("The final cost of your pizza will be: ${:,.2f}".format(final_cost)
          + " with tax included")
    print(" ")

    # Ask user if they want to calculate again
    print("Would you like to try with a different diameter?")
    user_answer = str(input("Y or N:"))

    if(user_answer == "Y" or "y"):

        main()


if __name__ == "__main__":
    main()
