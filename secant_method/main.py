#!/usr/bin/python


import sys
from math import *


# Put your function in the return value here.
def math_function(x):
	return cos(x) - x


def skip_lines(n_lines):
	for i in range(n_lines):
		print("")


def get_float_input(string):
	return float(raw_input(string))


def secant_method(x_n, x_n1):
	numerator = x_n1*math_function(x_n) - x_n*math_function(x_n1)
	denominator = math_function(x_n) - math_function(x_n1)
	return numerator/denominator


def find_root(x_n, x_n1, precision):
	max_iterations = 20

	for i in range(max_iterations):
		next_value = secant_method(x_n, x_n1)
		x_n1 = x_n
		x_n = next_value

		error = abs(x_n - x_n1)
		if error < precision:
			return [x_n, error, i]

	print("Reached Max Number of Iterations!!!! " + max_iterations)
	return [None, None, None]


def get_user_inputs():
	x_0 = get_float_input("Please, insert your X_0: ")
	x_1 = get_float_input("Please, insert your X_1: ")
	desired_precision = get_float_input("Please, insert your desired precision: ")
	return [x_0, x_1, desired_precision]


def print_results(root, error, iterations):
	print("Root: " + str(root))
	print("Error: " + str(error))
	print("Iterations: " + str(iterations))


if __name__ == '__main__':
	print("Numeric Calculus - Secant Method")
	skip_lines(2)

	[x_0, x_1, desired_precision] = get_user_inputs()

	[root, error, iterations] = find_root(x_1, x_0, desired_precision)

	print_results(root, error, iterations)

