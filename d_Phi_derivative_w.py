from b_Phi_function import phi_function
from c_Phi_derivative_x import phi_derivative_x
from sympy import diff


def phi_derivative_w(w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d, diff_parameter_d, order_phi_d):

    if order_phi_d == 0:
        int_parameters = w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d
        phi_func = phi_function(*int_parameters)
    elif order_phi_d > 0:
        int_parameters = w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d, order_phi_d
        phi_func = phi_derivative_x(*int_parameters)
    else:
        phi_func = 0

    result = diff(phi_func, diff_parameter_d)
    # print('phi_func = ', phi_func)
    # print('diff_parameter = ', diff_parameter_d)
    # print('dphi/dw = ', result)
    return result
