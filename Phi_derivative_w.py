from Phi_function import phi_function
from sympy import diff



def phi_derivative_w(w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d):
    int_parameters = w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d
    phi_func = phi_function(*int_parameters)
    phi_derivative = diff(phi_func, w_k_1_d)
    return phi_derivative
    return d
