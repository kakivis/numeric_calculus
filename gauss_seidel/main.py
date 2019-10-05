#!/usr/bin/python


from math import *


def get_float_input(string):
    return float(raw_input(string))


def get_int_input(string):
    return int(raw_input(string))


def get_user_inputs():
    n = get_int_input("Please, insert the number of equations: ")

    print("---------Coefficient Matrix---------")
    print("")
    a_matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            a = get_float_input("Please, insert your a" + str(i+1) + str(j+1) + " : ")
            line.append(a)

        a_matrix.append(line)

    print("---------Independent terms array---------")
    print("")
    b_matrix = []
    for i in range(n):
        b = get_float_input("Please, insert your b" + str(i+1) + " : ")
        b_matrix.append(b)

    print("---------Initial solution array---------")
    print("")
    initial_solution = []
    for i in range(n):
        x = get_float_input("Please, insert your x" + str(i+1) + " : ")
        initial_solution.append(x)

    precision = get_float_input("Please, insert your desired precision: ")
    return [a_matrix, b_matrix, initial_solution, precision]


def print_results(solution_array, error_array, iterations):
    print("")
    print("-------->Solution: " + str(solution_array))
    print("")
    print("-------->Error: " + str(error_array))
    print("")
    print("-------->Iterations: " + str(iterations+1))


def print_presentation():
    print("Numeric Calculus - Gauss Siedel Method")
    print("")
    print("")


def get_x_value(coefficients, b, solution, line, length):
    for i in range(length):
        if i != line:
            b = b - coefficients[i] * solution[i]

    return b / coefficients[line]


def calculate_error(old_solution, new_solution):
    error = []
    for i in range(len(old_solution)):
        error.append(abs(old_solution[i]-new_solution[i]))

    return error


def gauss_siedel_method(a_matrix, b_matrix, solution, precision):
    for iterations in range(256):
        n = len(b_matrix)
        old_solution = list(solution)
        for i in range(n):
            new_x = get_x_value(a_matrix[i], b_matrix[i], solution, i, n)
            solution[i] = new_x

        error_vector = calculate_error(old_solution, solution)
        should_stop = True
        for error in error_vector:
            if error > precision:
                should_stop = False

        if should_stop:
            break

    return [solution, error_vector, iterations]


if __name__ == '__main__':
    print_presentation()

    [a, b, init_solution, desired_precision] = get_user_inputs()
    [solutions, errors, iterations] = gauss_siedel_method(a, b, init_solution, desired_precision)

    print_results(solutions, errors, iterations)
