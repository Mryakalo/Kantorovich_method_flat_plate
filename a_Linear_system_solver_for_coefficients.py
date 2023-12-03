from sympy import symbols, solve


def calc_coefficients(w_k_1_c, dw_dx_k_1_c, w_k_c, dw_dx_k_c, x_k_1_c, x_k_c):
    b_0, b_1, b_2, b_3 = symbols('b_0 b_1 b_2 b_3')
    equation = [b_0 + x_k_1_c * b_1 + x_k_1_c ** 2 * b_2 + x_k_1_c ** 3 * b_3 - w_k_1_c,
                b_0 + x_k_c * b_1 + x_k_c ** 2 * b_2 + x_k_c ** 3 * b_3 - w_k_c,
                             b_1 + 2 * x_k_1_c * b_2 + 3 * x_k_1_c ** 2 * b_3 - dw_dx_k_1_c,
                             b_1 + 2 * x_k_c * b_2 + 3 * x_k_c ** 2 * b_3 - dw_dx_k_c]
    parameters = [b_0, b_1, b_2, b_3]
    solution = solve(equation, parameters, dict=True)
    # print(solution)
    b_0_k = str(solution)[str(solution).find('b_0:') + len('b_0:'): str(solution).rfind(', b_1')]
    b_1_k = str(solution)[str(solution).find('b_1:') + len('b_1:'): str(solution).rfind(', b_2')]
    b_2_k = str(solution)[str(solution).find('b_2:') + len('b_1:'): str(solution).rfind(', b_3')]
    b_3_k = str(solution)[str(solution).find('b_3:') + len('b_1:'): str(solution).rfind('}')]
    print('b0', b_0_k)
    print('b1', b_1_k)
    print('b2', b_2_k)
    print('b3', b_3_k)
    return b_0_k, b_1_k, b_2_k, b_3_k
