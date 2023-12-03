from f_Integral_dEs_dw import integral_des_dw
from sympy import symbols, sympify
from sympy import diff
import numpy as np

# В функции main_equations вычисляются коэффициенты к перемещениям и углам поворотов в главной СЛАУ,
# а также правая часть


def main_equations(node_amount: int, node_number: int, x_k_minus_1_in, x_k_in, x_k_plus_1_in, b_in, q_in, mu_in, d_in):
    coefficients = np.zeros((2, node_amount * 2))
    right_part_in = np.zeros(2)
    w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x = symbols('w_k_1 dw_dx_k_1 w_k dw_dx_k x_k_1 x_k x')

    # Вычисление коэффициентов для перемещений в интеграле, зависящем от фиk-1. Производная по wk (перемещение)
    integral_phi_k_minus_1_dw = integral_des_dw(b_in, q_in, mu_in, d_in, w_k_1, dw_dx_k_1, w_k, dw_dx_k,
                                                x_k_minus_1_in, x_k_in, x, w_k)
    print(integral_phi_k_minus_1_dw)
    coefficient_w_k_1 = diff(integral_phi_k_minus_1_dw, w_k_1)
    print(coefficient_w_k_1)
    coefficient_w_k = diff(integral_phi_k_minus_1_dw, w_k)
    print(coefficient_w_k)
    coefficient_dw_dx_k_1 = diff(integral_phi_k_minus_1_dw, dw_dx_k_1)
    print(coefficient_dw_dx_k_1)
    coefficient_dw_dx_k = diff(integral_phi_k_minus_1_dw, dw_dx_k)
    print(coefficient_dw_dx_k)

    right_part_in[0] = - float(sympify(str(integral_phi_k_minus_1_dw) + '-' + str(coefficient_w_k_1) + '*' + str(w_k_1) +\
                                                         '-' + str(coefficient_w_k) + '*' + str(w_k) +\
                                                         '-' + str(coefficient_dw_dx_k_1) + '*' + str(dw_dx_k_1) +\
                                                         '-' + str(coefficient_dw_dx_k) + '*' + str(dw_dx_k)))
    print(right_part_in[0])
    coefficients[0][node_number - 1 - 1] = float(coefficient_w_k_1)  # Еще раз минус 1, так как массив начинается с нуля
    coefficients[0][node_number - 1] = float(coefficient_w_k)
    coefficients[0][node_number - 1 - 1 + node_amount] = float(coefficient_dw_dx_k_1)
    coefficients[0][node_number - 1 + node_amount] = float(coefficient_dw_dx_k)
    print(coefficients)
    # Вычисление коэффициентов для перемещений в интеграле, зависящем от фиk. Производная по wk (перемещение)
    integral_phi_k_dw = integral_des_dw(b_in, q_in, mu_in, d_in, w_k_1, dw_dx_k_1, w_k, dw_dx_k,
                                        x_k_in, x_k_plus_1_in, x, w_k_1)
    print(integral_phi_k_dw)
    coefficient_w_k = diff(integral_phi_k_dw, w_k_1)
    print(coefficient_w_k)
    coefficient_w_k_plus_1 = diff(integral_phi_k_dw, w_k)
    print(coefficient_w_k_plus_1)
    coefficient_dw_dx_k = diff(integral_phi_k_dw, dw_dx_k_1)
    print(coefficient_dw_dx_k)
    coefficient_dw_dx_k_plus_1 = diff(integral_phi_k_dw, dw_dx_k)
    print(coefficient_dw_dx_k_plus_1)
    right_part_in[0] = right_part_in[0] - float(sympify(str(integral_phi_k_dw) +
                                                         '-' + str(coefficient_w_k) + '*' + str(w_k_1) +\
                                                         '-' + str(coefficient_w_k_plus_1) + '*' + str(w_k) +\
                                                         '-' + str(coefficient_dw_dx_k) + '*' + str(dw_dx_k_1) + \
                                                         '-' + str(coefficient_dw_dx_k_plus_1) + '*' + str(dw_dx_k)))
    print(right_part_in[0])
    coefficients[0][node_number - 1] = coefficients[0][node_number - 1] + float(coefficient_w_k)
    coefficients[0][node_number] = float(coefficient_w_k_plus_1)
    coefficients[0][node_number - 1 + node_amount] = coefficients[0][node_number - 1 +
                                                                     node_amount] + float(coefficient_dw_dx_k)
    coefficients[0][node_number + node_amount] = float(coefficient_dw_dx_k_plus_1)
    print(coefficients)
    # Вычисление коэффициентов для перемещений в интеграле, зависящем от фиk-1. Производная по dwk/dx (угол поворота)
    integral_phi_k_minus_1_dw_dx = integral_des_dw(b_in, q_in, mu_in, d_in, w_k_1, dw_dx_k_1, w_k, dw_dx_k,
                                                   x_k_minus_1_in, x_k_in, x, dw_dx_k_1)
    coefficient_w_k_1 = diff(integral_phi_k_minus_1_dw_dx, w_k_1)
    coefficient_w_k = diff(integral_phi_k_minus_1_dw_dx, w_k)
    coefficient_dw_dx_k_1 = diff(integral_phi_k_minus_1_dw_dx, dw_dx_k_1)
    coefficient_dw_dx_k = diff(integral_phi_k_minus_1_dw_dx, dw_dx_k)
    right_part_in[1] = - float(sympify(str(integral_phi_k_minus_1_dw_dx) + '-' + str(coefficient_w_k_1) + '*' + str(w_k_1) +\
                                                         '-' + str(coefficient_w_k) + '*' + str(w_k) +\
                                                         '-' + str(coefficient_dw_dx_k_1) + '*' + str(dw_dx_k_1) +\
                                                         '-' + str(coefficient_dw_dx_k) + '*' + str(dw_dx_k)))
    coefficients[1][node_number - 1 - 1] = float(coefficient_w_k_1)  # Еще раз минус 1, так как массив начинается с нуля
    coefficients[1][node_number - 1] = float(coefficient_w_k)
    coefficients[1][node_number - 1 - 1 + node_amount] = float(coefficient_dw_dx_k_1)
    coefficients[1][node_number - 1 + node_amount] = float(coefficient_dw_dx_k)

    # Вычисление коэффициентов для перемещений в интеграле, зависящем от фиk. Производная по dwk/dx (угол поворота)
    integral_phi_k_dw_dx = integral_des_dw(b_in, q_in, mu_in, d_in, w_k_1, dw_dx_k_1, w_k, dw_dx_k,
                                           x_k_in, x_k_plus_1_in, x, dw_dx_k_1)
    coefficient_w_k = diff(integral_phi_k_dw_dx, w_k_1)
    coefficient_w_k_plus_1 = diff(integral_phi_k_dw_dx, w_k)
    coefficient_dw_dx_k = diff(integral_phi_k_dw_dx, dw_dx_k_1)
    coefficient_dw_dx_k_plus_1 = diff(integral_phi_k_dw_dx, dw_dx_k)
    right_part_in[1] = right_part_in[1] - float(sympify(str(integral_phi_k_dw_dx) +
                                                         '-' + str(coefficient_w_k) + '*' + str(w_k_1) +\
                                                         '-' + str(coefficient_w_k_plus_1) + '*' + str(w_k) +\
                                                         '-' + str(coefficient_dw_dx_k) + '*' + str(dw_dx_k_1) + \
                                                         '-' + str(coefficient_dw_dx_k_plus_1) + '*' + str(dw_dx_k)))
    coefficients[1][node_number - 1] = coefficients[1][node_number - 1] + float(coefficient_w_k)
    coefficients[1][node_number] = float(coefficient_w_k_plus_1)
    coefficients[1][node_number - 1 + node_amount] = coefficients[1][node_number - 1 +
                                                                  node_amount] + float(coefficient_dw_dx_k)
    coefficients[1][node_number + node_amount] = float(coefficient_dw_dx_k_plus_1)
    print('Left part', coefficients)
    print('Right part', right_part_in)
    return coefficients, right_part_in
