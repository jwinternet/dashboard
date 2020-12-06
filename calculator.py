#!/usr/bin/env python3
"""Calculator"""

__author__ = "Jared Winter"
__started__ = "12/5/2020"
__revision__ = "v0.0.2"

import readline

import my_tools


class Calculator:
	"""
	This class takes two numbers and will either add, subtract, multiply or divide them.
	"""
	def __init__(self, num1, num2):
		self.num1 = int(num1)
		self.num2 = int(num2)

	def add(self):
		"""
		This method adds two numbers
		"""
		answer = self.num1 + self.num2
		print("\n", str(self.num1), "+", str(self.num2), "=", str(answer))

	def subtract(self):
		"""
		This method subtracts two numbers
		"""
		answer = self.num1 - self.num2
		print("\n", str(self.num1), "-", str(self.num2), "=", str(answer))

	def multiply(self):
		"""
		This method multiplies two numbers
		"""
		answer = self.num1 * self.num2
		print("\n", str(self.num1), "*", str(self.num2), "=", str(answer))

	def divide(self):
		"""
		This method divides two numbers
		"""
		answer = self.num1 / self.num2
		print("\n", str(self.num1), "/", str(self.num2), "=", str(answer))


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
			num1 = input("\n Enter 1st number: ")
			num2 = input(" Enter 2nd number: ")

			my_calculator = Calculator(num1, num2)

			if choice == "1":
				my_calculator.add()
			elif choice == "2":
				my_calculator.subtract()
			elif choice == "3":
				my_calculator.multiply()
			elif choice == "4":
				my_calculator.divide()

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
