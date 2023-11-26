from sympy import integrate
from Es_derivative_w import es_derivative_w


def integral(lower_in, upper_in, b_in, q_in, mu_in, d_in, w_k_1_in, dw_dx_k_1_in, w_k_in, dw_dx_k_in, x_k_1_in,
             x_k_in, x_in, diff_parameter_in):
    result = integrate(es_derivative_w(b_in, q_in, mu_in, d_in, w_k_1_in, dw_dx_k_1_in, w_k_in,
                                       dw_dx_k_in, x_k_1_in, x_k_in, x_in, diff_parameter_in),
                                       (x_in, lower_in, upper_in))
    return result
