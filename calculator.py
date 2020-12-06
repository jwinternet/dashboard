#!/usr/bin/env python3
"""Calculator"""

__author__ = "Jared Winter"
__started__ = "12/5/2020"
__revision__ = "v0.0.2"

import readline

import my_tools


def add(x, y):
	"""
	This function adds two numbers
	"""
	return x + y


def subtract(x, y):
	"""
	This function subtracts two numbers
	"""
	return x - y


def multiply(x, y):
	"""
	This function multiplies two numbers
	"""
	return x * y


def divide(x, y):
	"""
	This function divides two numbers
	"""
	return x / y


def main():
	"""
	Program make a simple calculator
	"""
	while True:
		my_tools.print_lines()
		print(
			"\t\t\t\t\t\t\t\t ",
			my_tools.PyColors.bold,
			my_tools.PyColors.Fg.dark_green,
			"Calculator Module",
			my_tools.PyColors.reset
		)
		choice = input(
			"\n Select an operation:"
			"\n 1) Add"
			"\n 2) Subtract"
			"\n 3) Multiply"
			"\n 4) Divide"
			"\n 5) Return To Main Menu"
			"\n\n Please select from one of the options listed above (1-5): "
		).strip()

		# Check if choice is one of the four options
		if int(choice) in range(1, 5):
			num1 = float(input("\n Enter first number: "))
			num2 = float(input(" Enter second number: "))

			if choice == "1":
				print("\n", num1, "+", num2, "=", add(num1, num2))

			elif choice == "2":
				print("\n", num1, "-", num2, "=", subtract(num1, num2))

			elif choice == "3":
				print("\n", num1, "*", num2, "=", multiply(num1, num2))

			elif choice == "4":
				print("\n", num1, "/", num2, "=", divide(num1, num2))
			input("\n\n Press enter to continue...").strip()
			break

		# Returns to the previous menu
		elif choice == "5":
			break

		#
		else:
			print(
				"\n",
				my_tools.PyColors.bold,
				my_tools.PyColors.Fg.light_yellow,
				"Invalid input, please try again...",
				my_tools.PyColors.reset
			)


if __name__ == "__main__":
	main()
