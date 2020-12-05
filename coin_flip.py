#!/usr/bin/env python3
"""Coin Flip"""

__author__ = "Jared Winter"
__started__ = "12/4/2020"
__revision__ = "v0.0.3"

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
			"\n\t\t\t\t ",
			my_tools.PyColors.Bg.light_blue,
			"Coin Flip",
			my_tools.PyColors.reset,
			"\n\n Heads or Tails, call it...\n"
		)
		input().strip()
		random_result = random.randint(1, 2)
		if random_result == 1:
			print(" HEADS!\n\n")
		elif random_result == 2:
			print(" TAILS!\n\n")
		choice = input(
			" Play again or return to previous menu? Y/N\n ").strip()
		if "y" in choice.lower():
			continue
		elif "n" in choice.lower():
			break


if __name__ == "__main__":
	main()
