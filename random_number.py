#!/usr/bin/env python3
"""Random Number Generator"""

__author__ = "Jared Winter"
__started__ = "12/4/2020"
__revision__ = "v0.0.4"

import random
import readline

import my_tools


def main():
	"""
	Includes several games for fun, including coin flip and random number generator that both
	return random results
	"""
	while True:
		my_tools.print_lines()
		print(
			"\n\t\t\t ",
			my_tools.PyColors.Bg.light_blue,
			"Random Number Generator",
			my_tools.PyColors.reset,
			"\n\n So you want a random number, in what range?"
		)
		first_number = input(" Start of range: ").strip()
		second_number = input(" End of range: ").strip()
		random_result = random.randint(int(first_number), int(second_number))
		print("\n\n Your random number is: " + str(random_result) + "\n\n")
		choice = input(" Go again or return to previous menu? Y/N\n ").strip()
		if "y" in choice.lower():
			continue
		elif "n" in choice.lower():
			break


if __name__ == "__main__":
	main()
