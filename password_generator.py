#!/usr/bin/env python3
"""Password Generator"""

__author__ = "Jared Winter"
__started__ = "12/4/2020"
__revision__ = "v0.0.1"

import random
import readline

import my_tools


def main():
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
		"\t\t\t\t\t\t\t",
		my_tools.PyColors.bold,
		my_tools.PyColors.Fg.light_yellow,
		my_tools.PyColors.Bg.dark_blue,
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


if __name__ == "__main__":
	main()
