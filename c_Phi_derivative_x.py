from b_Phi_function import phi_function
from sympy import diff


def phi_derivative_x(w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d, order_d):
    int_parameters = w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d
    phi_func = phi_function(*int_parameters)
    phi_derivative_1st = diff(phi_func, x_d)
    phi_derivative_2nd = diff(phi_derivative_1st, x_d)
    phi_derivative_3rd = diff(phi_derivative_2nd, x_d)
    if order_d == 1:
        result = phi_derivative_1st
    elif order_d == 2:
        result = phi_derivative_2nd
    elif order_d == 3:
        result = phi_derivative_3rd
    else:
        result = 'Неправильный порядок производной'
    # print('dphi/dx = ', result)
    return result
