from Phi_function import phi_function
from sympy import symbols, diff


def phi_derivative_x(w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d,
                     x_k_1_d, x_k_d):
    x = symbols('x')
    int_parameters = w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x
    phi_func = phi_function(*int_parameters)
    phi_derivative = diff(phi_func, x)
    return phi_derivative
