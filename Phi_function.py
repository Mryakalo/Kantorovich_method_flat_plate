from Linear_system_solver_for_coefficients import calc_coefficients


def phi_function(w_k_1_p, dw_dx_k_1_p, w_k_p, dw_dx_k_p, x_k_1_p, x_k_p, x_p):
    int_parameters = w_k_1_p, dw_dx_k_1_p, w_k_p, dw_dx_k_p, x_k_1_p, x_k_p
    b_0, b_1, b_2, b_3 = calc_coefficients(*int_parameters)
    x_p_str = str(x_p)
    phi = b_0 + '+' + b_1 + '*' + x_p_str + '+' + b_2 + '*' + x_p_str + '** 2' + '+' + b_3 + '*' + x_p_str + '** 3'
    return phi
