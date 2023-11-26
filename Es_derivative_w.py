from Phi_function import phi_function
from Phi_derivative_x import phi_derivative_x
from Phi_derivative_w import phi_derivative_w


def es_derivative_w(b_es, q_es, mu_es, d_es, w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d,
                    x_k_d, x_d, diff_parameter_d):
    a_1 = 3 * b_es / 8
    a_2 = (2 * 3.14 ** 4) / b_es ** 3
    a_3 = - mu_es * 3.14 ** 2 / b_es
    a_4 = (1 - mu_es) * 3.14 ** 2 / b_es
    q_1 = b_es * q_es / d_es
    # Функция фи
    phi = phi_function(w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d)
    # Первая производная функции фи по x
    phi_1 = phi_derivative_x(w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d, 1)
    # Вторая производная функции фи по x
    phi_2 = phi_derivative_x(w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d, 2)
    # Производная функции фи по w
    d_phi_d_w = phi_derivative_w(w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d, diff_parameter_d, 0)
    # Производная первой производной фи по х по w
    d_phi_1_d_w = phi_derivative_w(w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d, diff_parameter_d, 1)
    # Производная второй производной фи по х по w
    d_phi_2_d_w = phi_derivative_w(w_k_1_d, dw_dx_k_1_d, w_k_d, dw_dx_k_d, x_k_1_d, x_k_d, x_d, diff_parameter_d, 2)
    # Вариация функционала Es по w (пункт e, уравнение 7)
    de_dw = ('2 *' + str(a_1) + '*' + str(phi_2) + '*' + str(d_phi_2_d_w) + '+'
             + '2 *' + str(a_2) + '*' + str(phi) + '*' + str(d_phi_d_w) + '+'
             + str(a_3) + '*' + str(phi_2) + '*' + str(d_phi_d_w) + '+'
             + str(a_3) + '*' + str(phi) + '*' + str(d_phi_2_d_w) + '+'
             + '2 *' + str(a_4) + '*' + str(phi_1) + '*' + str(d_phi_1_d_w) + '-'
             + str(q_1) + '*' + str(d_phi_d_w))

    return de_dw
