from b_Phi_function import phi_function
from a_Linear_system_solver_for_coefficients import calc_coefficients
from d_Phi_derivative_w import phi_derivative_w
from sympy import symbols, integrate
from e_Es_derivative_w import es_derivative_w
from f_Integral_dEs_dw import integral_des_dw
from scipy.integrate import quad
import numpy as np
from g_Main_equations import main_equations

# Исходные параметры пластины
a_plate: float = 6  # Длина в направлении x [м]
b_plate: float = 40  # Ширина в направлении y [м]
h_plate: float = 0.2  # Толщина пластины [м]
q_load: float = 0.01  # Распределенная нагрузка [кН/м2]
E_modulus: float = 40000  # Модуль деформации материала [МПа]
mu: float = 0.2  # Коэффициент пуассона
n_elem: int = 3  # Количество элементов, на которые разбивается пластина в направлении x
n_nodes: int = n_elem + 1
d_stiffness: float = E_modulus * h_plate ** 3 / (12 * (1 - mu ** 2))

# Сбор основной системы уравнений
left_part = np.zeros((n_nodes * 2, n_nodes * 2))
right_part = np.zeros(n_nodes * 2)
for i in range(1,n_nodes - 1, 1):
    print(i)
    x_k_minus_1 = a_plate / n_elem * (i - 1)
    print(x_k_minus_1)
    x_k = a_plate / n_elem * i
    print(x_k)
    x_k_plus_1 = a_plate / n_elem * (i + 1)
    print(x_k_plus_1)
    left_part, right_part = main_equations(n_nodes,
                                           i + 1,
                                           x_k_minus_1,
                                           x_k,
                                           x_k_plus_1,
                                           b_plate,
                                           q_load,
                                           mu,
                                           d_stiffness)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(left_part)



# w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x = symbols('w_k_1 dw_dx_k_1 w_k dw_dx_k x_k_1 x_k x')
#
# print(phi_derivative_w(w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x, w_k_1, 0))
# print(phi_derivative_w(w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x, w_k_1, 1))
# print(phi_derivative_w(w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x, w_k_1, 2))
#
# print(es_derivative_w(b_plate, q_load, mu, d_stiffness, w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x, w_k_1))
# print(integral_des_dw(x_k_1, x_k, b_plate, q_load, mu, d_stiffness, w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x, w_k_1))
# result = integrate(integral(w_k_1, x, w_k), (x, x_k_1, x_k))
# print(result)
