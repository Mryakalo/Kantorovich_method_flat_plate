from sympy import sympify, diff, lambdify, symbols
import numpy as np

from b_Phi_function import phi_function
from c_Phi_derivative_x import phi_derivative_x


def bound_cond_equations(a_1_in, a_3_in, a_4_in, x_k_1_in, x_k_in, x_in):
    coefficients = np.zeros((2, 2 * 2))

    w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x = symbols('w_k_1 dw_dx_k_1 w_k dw_dx_k x_k_1 x_k x')

    # Функция фи
    phi = phi_function(w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x)
    # Первая производная функции фи по x
    phi_1 = phi_derivative_x(w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x, 1)
    # Вторая производная функции фи по x
    phi_2 = phi_derivative_x(w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x, 2)
    # Третья производная функции фи по x
    phi_3 = phi_derivative_x(w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x, 3)
    a_1_str = str(a_1_in)
    a_3_str = str(a_3_in)
    a_4_str = str(a_4_in)
    phi_str = '(' + str(phi) + ')'
    # print(phi_str)
    phi_1_str = '(' + str(phi_1) + ')'
    # print(phi_1_str)
    phi_2_str = '(' + str(phi_2) + ')'
    # print(phi_2_str)
    phi_3_str = '(' + str(phi_3) + ')'
    # print(phi_3_str)
    boundary_equation_1 = sympify(a_1_str + '*' + phi_2_str + '+' + a_3_str + '*' + phi_str)
    boundary_equation_2 = sympify('2. *' + a_1_str + '*' + phi_3_str + '+' + '(' + a_3_str + '-'
                                  + '2. *' + a_4_str + ')' + '*' + phi_1_str)

    coefficient_w_k_1 = diff(boundary_equation_1, w_k_1)
    # print(coefficient_w_k_1)
    coefficient_w_k = diff(boundary_equation_1, w_k)
    # print(coefficient_w_k)
    coefficient_dw_dx_k_1 = diff(boundary_equation_1, dw_dx_k_1)
    # print(coefficient_dw_dx_k_1)
    coefficient_dw_dx_k = diff(boundary_equation_1, dw_dx_k)
    # print(coefficient_dw_dx_k)

    lambda_equation = lambdify([x, x_k_1, x_k], coefficient_w_k_1)
    coefficients[0][0] = lambda_equation(x_in, x_k_1_in, x_k_in)

    lambda_equation = lambdify([x, x_k_1, x_k], coefficient_w_k)
    coefficients[0][1] = lambda_equation(x_in, x_k_1_in, x_k_in)

    lambda_equation = lambdify([x, x_k_1, x_k], coefficient_dw_dx_k_1)
    coefficients[0][2] = lambda_equation(x_in, x_k_1_in, x_k_in)

    lambda_equation = lambdify([x, x_k_1, x_k], coefficient_dw_dx_k)
    coefficients[0][3] = lambda_equation(x_in, x_k_1_in, x_k_in)

    coefficient_w_k_1 = diff(boundary_equation_2, w_k_1)
    # print(coefficient_w_k_1)
    coefficient_w_k = diff(boundary_equation_2, w_k)
    # print(coefficient_w_k)
    coefficient_dw_dx_k_1 = diff(boundary_equation_2, dw_dx_k_1)
    # print(coefficient_dw_dx_k_1)
    coefficient_dw_dx_k = diff(boundary_equation_2, dw_dx_k)
    # print(coefficient_dw_dx_k)

    lambda_equation = lambdify([x, x_k_1, x_k], coefficient_w_k_1)
    coefficients[1][0] = lambda_equation(x_in, x_k_1_in, x_k_in)

    lambda_equation = lambdify([x, x_k_1, x_k], coefficient_w_k)
    coefficients[1][1] = lambda_equation(x_in, x_k_1_in, x_k_in)

    lambda_equation = lambdify([x, x_k_1, x_k], coefficient_dw_dx_k_1)
    coefficients[1][2] = lambda_equation(x_in, x_k_1_in, x_k_in)

    lambda_equation = lambdify([x, x_k_1, x_k], coefficient_dw_dx_k)
    coefficients[1][3] = lambda_equation(x_in, x_k_1_in, x_k_in)


    # print(right_part_in)
    return coefficients
