#!/usr/bin/env python3
# Created By: Sam V
# Date: Oct 13th, 2026
# This program calculates the sum of all numbers from 0 to a user-defined positive number.


def main():
    # Step 1: Get a valid positive number
    while True:
        try:
            user_input = int(input("Enter a positive number: "))
            if user_input < 0:
                print("Error: Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")

    # Step 2: Initialize our variables
    total_sum = 0
    counter = 0

    # Step 3: Run the while loop to add the numbers
    while counter <= user_input:
        total_sum = total_sum + counter
        counter = counter + 1

    # Step 4: Print the result
    print(f"The sum of all numbers from 0 to {user_input} is: {total_sum}")


if __name__ == "__main__":
    main()
