#!/usr/bin/env python3
"""Dashboard"""

__author__ = "Jared Winter"
__started__ = "12/1/2020"
__revision__ = "v0.0.3"

import sys

import my_tools
import password_generator
import coin_flip
import random_number


def main():
	"""
	Main module for all others, presents menus in loops for easy end-user accessibility and
	reusability.
	:return:
	:rtype:
	"""
	# Try statement for catching errors
	try:
		# Continuous while loop that keeps the program going indefinitely
		while True:
			# Prints a long yellow line to separate sections of the menu
			my_tools.print_lines()
			# Program's banner, containing the name, version and date
			print(
				"\t\t\t\t\t\t\t",
				my_tools.PyColors.bold,
				my_tools.PyColors.Fg.light_yellow,
				" <<< Dashboard >>>",
				my_tools.PyColors.reset,
				"\n\n\t\t\t\t\t",
				my_tools.PyColors.Fg.light_green,
				"  Project Version <|> Last Updated\n\t\t\t\t\t\t\t",
				"  0.0.3         12/05/2020",
				my_tools.PyColors.reset
			)

			# Presents the user with a menu of options to choose from
			first_choice = input(
				"\n 1) General"
				"\n 2) Game of Chance"
				"\n 3) Release Notes"
				"\n 4) Quit"
				"\n\n Please select from one of the options listed above (1-4): "
			).strip()

			#
			if first_choice == "1":
				while True:
					my_tools.print_lines()
					print(
						"\t\t\t\t\t\t\t ",
						my_tools.PyColors.Bg.light_blue,
						"General Module",
						my_tools.PyColors.reset
					)

					second_choice = input(
						"\n 1) Password Generator"
						"\n 2) Coin Flip"
						"\n 3) Random Number Generator"
						"\n 4) Return To Main Menu"
						"\n\n Please select from one of the options listed above (1-4): "
					).strip()

					#
					if second_choice == "1":
						password_generator.main()

					#
					elif second_choice == "2":
						coin_flip.main()

					#
					elif second_choice == "3":
						random_number.main()

					# Returns the user to the main menu
					elif second_choice == "4":
						break

			#
			elif first_choice == "2":

				#
				while True:
					my_tools.print_lines()
					print(
						"\n\t\t\t ",
						my_tools.PyColors.Bg.light_blue,
						"Test 2 Module",
						my_tools.PyColors.reset
					)
					second_choice = input(
						"\n 1) Test 1"
						"\n 2) Test 2"
						"\n 3) About Module"
						"\n 4) Return To Main Menu"
						"\n\n Please select from one of the options listed above (1-4): "
					).strip()
					try:
						#
						if int(second_choice) in range(1, 3):
							# Test.Test(second_choice)
							pass

						#
						elif second_choice == "3":
							# Test.Test.about_module()
							pass

						# Returns to the previous menu
						elif second_choice == "4":
							break

					# Protects the program from erroneous data being entered
					except ValueError:
						continue

			# How to section on reporting any issues with this program
			elif first_choice == "3":
				my_tools.print_lines()
				print(
					"\n\t\t\t ",
					my_tools.PyColors.Bg.light_blue,
					"Version 0.0.0 Release Notes",
					my_tools.PyColors.reset,
					"\n\n New Features:"
					"\n"
				)
				input("\n\n Press enter to continue...").strip()
				continue

			# Enables to user to exit the program without a keyboard interrupt
			elif first_choice == "4":
				print("\n\n ...Exiting program\n\n")
				sys.exit(0)

	# Gracefully ends the program when the user hits the 'control + c' keys
	except KeyboardInterrupt:
		print("\n\n ...Exiting program\n\n")
		sys.exit(0)


if __name__ == "__main__":
	main()
