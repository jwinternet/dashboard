#!/usr/bin/env python3

__author__ = "Jared Winter"
__started__ = "12/1/2020"
__revision__ = "v0.0.1"

import random
import readline

import my_tools


def password_generator():
	"""
	Creates a new password using random characters
	"""
	# Pool of characters that are drawn upon to create a password
	chars_vowels = "aeiouAEIUaeiu"
	all_chars = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
	chars_number = "0123456789"
	chars_symbol = "@#$!"
	# Referencing the strings above, 8 total characters are taken from the strings in a random
	# fashion, with this being done 10 total times
	play = 0
	my_tools.print_lines()
	print(
		"\n\t\t\t\t ",
		my_tools.PyColors.Bg.light_blue,
		"Password Generator",
		my_tools.PyColors.reset,
		"\n\n Below are 10 randomly generated passwords:\n"
	)
	while play < 10:
		new_password = random.choice(chars_vowels)
		new_password += random.choice(all_chars)
		new_password += random.choice(chars_number)
		new_password += random.choice(chars_symbol)
		new_password += random.choice(chars_vowels)
		new_password += random.choice(all_chars)
		new_password += random.choice(chars_vowels)
		new_password += random.choice(chars_vowels)
		password_list = list(new_password)
		random.SystemRandom().shuffle(password_list)
		new_password = "".join(password_list)
		print(" " + new_password)
		play += 1
	input("\n\n Press enter to continue...").strip()


def game_of_chance():
	"""
	Includes several games for fun, including coin flip and random number generator that both
	return random results
	"""
	while True:
		my_tools.print_lines()
		print(
			"\n\t\t\t\t ",
			my_tools.PyColors.Bg.light_blue,
			"Game of Chance",
			my_tools.PyColors.reset
		)
		choice = input(
			"\n 1) Coin Flip"
			"\n 2) Random Number Generator"
			"\n 3) Return To Main Menu"
			"\n\n Please specify one of the options listed above (1-3): "
		).strip()

		# A coin toss program that returns either heads or tails, in a randomly generated fashion
		if choice == "1":
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

		# Asks the user to enter in a low number and a high number, and a randomly generated
		# number in that range is returned
		elif choice == "2":
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

		# Returns to the previous menu
		elif choice == "3":
			break


def about_module():
	"""
	Provides a basic overview and some 'tips and tricks' that may be useful to any end user of
	this module
	"""
	my_tools.print_lines()
	print(
		"\n\t\t\t\t ",
		my_tools.PyColors.Bg.dark_yellow,
		"About Module",
		my_tools.PyColors.reset,
		"\n\n",
		my_tools.PyColors.Fg.light_cyan,
		my_tools.PyColors.bold,
		"Purpose",
		my_tools.PyColors.reset
	)
	summary = """Additional programs that have no network automation focus, but are instead 
	included for fun."""
	my_tools.text_wrapper(summary, "\n ", " ")
	print(
		"\n",
		my_tools.PyColors.Fg.light_cyan,
		my_tools.PyColors.bold,
		"Sub-Modules",
		my_tools.PyColors.reset
	)
	extra_one = """'Password Generator' – Creates a randomized password that conforms to the 
	standards of PNC Bank’s password requirements."""
	my_tools.text_wrapper(extra_one, "\n - ", "\t ")
	extra_two = """'Coin Flip' – You specify if you want to bet on heads or tails, 
	with a randomized result being the end-result."""
	my_tools.text_wrapper(extra_two, "\n - ", "\t ")
	extra_three = """'Random Number Generator' – Enter a beginning range and an ending range, 
	a random number between those numbers will be created."""
	my_tools.text_wrapper(extra_three, "\n - ", "\t ")
	input("\n\n Press enter to continue...").strip()
