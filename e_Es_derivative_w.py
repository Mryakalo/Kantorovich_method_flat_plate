from b_Phi_function import phi_function
from c_Phi_derivative_x import phi_derivative_x
from d_Phi_derivative_w import phi_derivative_w
from sympy import sympify


def es_derivative_w(a_1_in, a_2_in, a_3_in, a_4_in, q_1_in, w_k_1_es, dw_dx_k_1_es, w_k_es, dw_dx_k_es, x_k_1_es,
                    x_k_es, x_es, diff_parameter_es):
    # Функция фи
    phi = phi_function(w_k_1_es, dw_dx_k_1_es, w_k_es, dw_dx_k_es, x_k_1_es, x_k_es, x_es)
    # Первая производная функции фи по x
    phi_1 = phi_derivative_x(w_k_1_es, dw_dx_k_1_es, w_k_es, dw_dx_k_es, x_k_1_es, x_k_es, x_es, 1)
    # Вторая производная функции фи по x
    phi_2 = phi_derivative_x(w_k_1_es, dw_dx_k_1_es, w_k_es, dw_dx_k_es, x_k_1_es, x_k_es, x_es, 2)
    # Производная функции фи по w
    d_phi_d_w = phi_derivative_w(w_k_1_es, dw_dx_k_1_es, w_k_es, dw_dx_k_es,
                                 x_k_1_es, x_k_es, x_es, diff_parameter_es, 0)
    # Производная первой производной фи по х по w
    d_phi_1_d_w = phi_derivative_w(w_k_1_es, dw_dx_k_1_es, w_k_es, dw_dx_k_es,
                                   x_k_1_es, x_k_es, x_es, diff_parameter_es, 1)
    # Производная второй производной фи по х по w
    d_phi_2_d_w = phi_derivative_w(w_k_1_es, dw_dx_k_1_es, w_k_es, dw_dx_k_es,
                                   x_k_1_es, x_k_es, x_es, diff_parameter_es, 2)
    # Вариация функционала Es по w (пункт e, уравнение 7)
    a_1_str = str(a_1_in)
    a_2_str = str(a_2_in)
    a_3_str = str(a_3_in)
    a_4_str = str(a_4_in)
    q_1_str = str(q_1_in)
    phi_2_str = '(' + str(phi_2) + ')'
    # print(phi_2_str)
    d_phi_2_d_w_str = '(' + str(d_phi_2_d_w) + ')'
    # print(d_phi_2_d_w_str)
    phi_str = '(' + str(phi) + ')'
    # print(phi_str)
    d_phi_d_w_str = '(' + str(d_phi_d_w) + ')'
    # print(d_phi_d_w_str)
    phi_1_str = '(' + str(phi_1) + ')'
    # print(phi_1_str)
    d_phi_1_d_w_str = '(' + str(d_phi_1_d_w) + ')'
    # print(d_phi_1_d_w_str)
    de_dw = sympify('2 *' + a_1_str + '*' + phi_2_str + '*' + d_phi_2_d_w_str + '+'
             + '2 *' + a_2_str + '*' + phi_str + '*' + d_phi_d_w_str + '+'
             + a_3_str + '*' + phi_2_str + '*' + d_phi_d_w_str + '+'
             + a_3_str + '*' + phi_str + '*' + d_phi_2_d_w_str + '+'
             + '2 *' + a_4_str + '*' + phi_1_str + '*' + d_phi_1_d_w_str + '-'
             + q_1_str + '*' + d_phi_d_w_str)
    # print('dE/dw', de_dw)
    return de_dw
