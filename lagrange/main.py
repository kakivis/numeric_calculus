#!/usr/bin/python


def get_float_array_input(string):
	string_input = raw_input(string)
	input_list = string_input.split()
	input_list = [float(a) for a in input_list]
	return input_list


def get_float_input(string):
	return float(raw_input(string))


def get_int_input(string):
	return int(raw_input(string))


def find_coeficients(n, x_vector, x_barra):
	coefficients = []
	numerator = 1
	denominator = 1
	for i in range(0, n+1):
		for j in range(0, n+1):
			if j == i:
				continue
			numerator = numerator*(x_barra-x_vector[j])
			denominator = denominator*(x_vector[i]-x_vector[j])

		coefficients.append(numerator/denominator)
		numerator = 1
		denominator = 1
	return coefficients


def evaluate_polinomial(n, y, coefficients):
	value = 0
	for i in range(0, n+1):
		value = value + y[i]*coefficients[i]
	return value


def lagrange_method(n, x, y, x_barra):
	coefficients = find_coeficients(n, x, x_barra)
	result = evaluate_polinomial(n, y, coefficients)
	return result


def get_user_inputs():
	n = get_int_input("Please, insert your n: ")
	x = get_float_array_input("Please, insert your X array separated by spaces: ")
	y = get_float_array_input("Please, insert your y array separated by spaces: ")
	x_barra = get_float_input("Please, insert your x barra: ")
	return [n, x, y, x_barra]


def print_results(y_barra):
	print("y_barra: " + str(y_barra))


def print_presentation():
	print("Numeric Calculus - Lagrange Method")
	print("")
	print("")


if __name__ == '__main__':
	print_presentation()

	[n, x, y, x_barra] = get_user_inputs()

	y_barra = lagrange_method(n, x, y, x_barra)

	print_results(y_barra)

