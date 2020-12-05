#!/usr/bin/env python3
"""My Tools"""

__author__ = "Jared Winter"
__started__ = "12/1/2020"
__revision__ = "v0.0.3"

import datetime
import getpass
import os
import socket
import subprocess
import textwrap
import time


class PyColors:
	"""
	Class for adding colors and formatting to printed text to other modules.
	"""
	reset = "\033[00m"
	bold = "\033[01m"
	underline = "\033[04m"
	slow_blink = "\033[05m"
	dim = "\033[2m"
	reverse = "\033[7m"
	hidden = "\033[8m"

	class Fg:
		"""
		Class for adding foreground colors to printed text in other modules.
		"""
		black = "\033[30m"
		dark_red = "\033[31m"
		dark_green = "\033[32m"
		dark_yellow = "\033[33m"
		dark_blue = "\033[34m"
		dark_purple = "\033[35m"
		dark_cyan = "\033[36m"
		dark_grey = "\033[90m"
		light_grey = "\033[37m"
		light_red = "\033[91m"
		light_green = "\033[92m"
		light_yellow = "\033[93m"
		light_blue = "\033[94m"
		light_purple = "\033[95m"
		light_cyan = "\033[96m"
		light_white = "\033[97m"
		# orange = "\033[48:2:255:165:0m%s"

	class Bg:
		"""
		Class for adding background colors to printed text in other modules.
		"""
		black = "\033[40m"
		dark_red = "\033[41m"
		dark_green = "\033[42m"
		dark_yellow = "\033[43m"
		dark_blue = "\033[44m"
		dark_purple = "\033[45m"
		dark_cyan = "\033[46m"
		dark_grey = "\033[100m"
		light_grey = "\033[47m"
		light_red = "\033[101m"
		light_green = "\033[102m"
		light_yellow = "\033[103m"
		light_blue = "\033[104m"
		light_purple = "\033[105m"
		light_cyan = "\033[106m"
		light_white = "\033[107m"


def hostname_resolves(hostname):
	"""
	Returns a boolean value on whether a DNS record exists or not (1 being true, and 2 being false).
	:param str hostname: Device hostname
	:return int: Returns a boolean value depending on the pings results
	"""
	try:
		socket.gethostbyname(hostname)
		return 1
	except socket.error:
		return 0


def resolve_ip(host):
	"""
	"""
	result = os.popen("dig 0.0.0.0 axfr | grep -F " + host).readlines()
	print(result)
	if len(result) > 0:
		partitioned_result = result.rpartition(" ")[0]
		print(partitioned_result)
		return partitioned_result
	else:
		second_result = os.popen("dig @0.0.0.0 axfr | grep -F " + host).readlines()
	if len(second_result) > 0:
		partitioned_result = second_result.rpartition(" ")[0]
		return partitioned_result
	else:
		return "UNKNOWN"


def get_ip(node):
	"""
	Takes a hostname and resolves it to an IP address.
	:param str node: Device hostname
	:return str address_two: Returns a properly concatenated string
	"""

	try:
		address_one = socket.gethostbyname_ex(node)
		address_two = str(address_one[2]).replace("['", "").replace("']", "")
		return address_two
	except socket.gaierror:
		print("\n" + node + " - does not exist in DNS\n\n")


def get_hostname(node):
	"""
	Takes a IP address and resolves it to an hostname.
	:param node: Device IP address
	:return str address_two: Returns a properly concatenated string
	"""
	try:
		address_one = socket.gethostbyaddr(node)
		address_two = address_one[0]
		return address_two
	except socket.gaierror:
		return "UNKNOWN"
	except socket.herror:
		return "UNKNOWN"


def can_ping_ip(hostname):
	"""
	Attempts to ping a hostname.
	:param str hostname: Device hostname
	:return str pingable: Returns the ping results
	"""
	pingable = subprocess.call(["ping", "-q", "-c", "3", hostname], stdout=subprocess.DEVNULL)
	return pingable


def get_ip_and_ping(hostname):
	"""
	Attempts to resolve and then ping a hostname.
	:param str hostname: Device hostname
	:return int: Returns a boolean value depending on the pings results
	"""
	hostname_ip = get_ip(hostname)
	hostname_pingable = can_ping_ip(hostname_ip)
	if hostname_pingable == 0:
		return 0
	else:
		return 1


def resolve_and_get_ip(hostname):
	"""
	Checks if a hostname is in DNS and then resolves that hostname to an IP and attempts to
	return the IP address.
	:param str hostname: Device hostname
	:return str hostname_ip: Resolved IP address or a False value
	"""
	host_resolves = hostname_resolves(hostname)
	if host_resolves == 1:
		hostname_ip = get_ip(hostname)
		return hostname_ip
	if host_resolves == 0:
		return False


def resolve_and_ping(hostname):
	"""
	Attempts to resolve and then ping an IP address.
	:param str hostname: Device hostname
	:return int: Returns a boolean value depending on the DNS resolution and ping results
	"""
	host_resolves = hostname_resolves(hostname)
	if host_resolves == 1:
		hostname_ip = get_ip(hostname)
		hostname_pingable = can_ping_ip(hostname_ip)
		if hostname_pingable == 0:
			return 0
		else:
			return 1
	else:
		return 2


def get_username():
	"""
	Function for storing a username as a variable.
	:return str username: Returns a properly concatenated string
	"""
	username = input(" Username: ").strip()
	return username


def get_password():
	"""
	Function for storing a password as a variable, utilizing Getpass.
	:return str password: Returns a properly concatenated string
	"""
	password = getpass.getpass(" Password: ").strip()
	return password


def get_today():
	"""
	Function for providing the today's date in a month and day format, ex. "May 21".
	:return str today: Returns a properly concatenated string
	"""
	today = time.strftime("%b %d", time.localtime())
	return today


def get_now():
	"""
	Function for providing the time and date, ex.
	Time: 06:31:52 Date: 05-21-2020
	"""
	now = time.strftime("Time: %H:%M:%S Date: %m-%d-%Y", time.localtime())
	print(
		"\n\n",
		PyColors.Bg.dark_cyan,
		now,
		PyColors.reset,
		"\n"
	)


def get_yesterday():
	"""
	Function for providing the previous day's date in a month and day format, ex. 'May 20'.
	:return str yesterday: Returns a properly concatenated string
	"""
	yesterday = datetime.datetime.strftime(
		datetime.datetime.now() - datetime.timedelta(1),
		"%b %d"
	)
	return yesterday


def get_two_days_ago():
	"""
	Function for providing the date from 2 days ago in a month and day format, ex. 'May 20'.
	:return str yesterday: Returns a properly concatenated string
	"""
	yesterday = datetime.datetime.strftime(
		datetime.datetime.now() - datetime.timedelta(2),
		"%b %d"
	)
	return yesterday


def print_lines():
	"""
	Prints a long dark yellow line to the screen.
	"""
	print(
		"\n",
		PyColors.bold,
		PyColors.Fg.dark_red,
		"_" * 80,
		PyColors.reset,
		"\n\n"
	)


def print_arrows():
	"""
	Prints a long light green line (made up of dashes, arrows and spaces) to the screen.
	"""
	print(
		"\n\n\t",
		PyColors.bold,
		PyColors.Fg.light_green,
		" <<- --- - --- - <-----> - --- - --- ->>",
		PyColors.reset,
		"\n\n"
	)


def text_wrapper(string, initial, subsequent):
	"""
	Utilizing the Textwrap library, a multi-line string is formatted by removing whitespace,
	newlines, setting an indent and width
	:param str string: The string to be formatted
	:param str initial: The initial indent to be added when formatting the string
	:param str subsequent: The subsequent indent to be added when formatting the string
	"""
	new_string = "\n".join([line.strip() for line in string.splitlines()])
	wrapper = textwrap.TextWrapper(
		width=82,
		initial_indent=initial,
		subsequent_indent=subsequent,
		drop_whitespace=True
	)
	new_wrapper = wrapper.fill(new_string.strip("\n"))
	print(new_wrapper)
