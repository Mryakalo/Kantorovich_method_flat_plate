from sympy import integrate
from e_Es_derivative_w import es_derivative_w


def integral_des_dw(a_1_in, a_2_in, a_3_in, a_4_in, q_1_in, w_k_1_in, dw_dx_k_1_in, w_k_in, dw_dx_k_in, x_k_1_in,
                    x_k_in, x_in, diff_parameter_in):
    result = integrate(es_derivative_w(a_1_in, a_2_in, a_3_in, a_4_in, q_1_in, w_k_1_in, dw_dx_k_1_in, w_k_in,
                                       dw_dx_k_in, x_k_1_in, x_k_in, x_in, diff_parameter_in),
                       (x_in, x_k_1_in, x_k_in))
    # print('integral dEs/',diff_parameter_in, '--->', result)
    return result
