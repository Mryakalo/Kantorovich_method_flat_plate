import numpy as np
from g_Main_equations import main_equations
from Phi_bound_cond_equations import bound_cond_equations


# Исходные параметры пластины
a_plate: float = 6  # Длина в направлении x [м]
b_plate: float = 40  # Ширина в направлении y [м]
h_plate: float = 0.2  # Толщина пластины [м]
q_load: float = 0.01  # Распределенная нагрузка [МН/м2]
E_modulus: float = 40000  # Модуль деформации материала [МПа]
mu: float = 0.2  # Коэффициент Пуассона
n_elem: int = 40  # Количество элементов, на которые разбивается пластина в направлении x
n_nodes: int = n_elem + 1
d_stiffness: float = E_modulus * h_plate ** 3 / (12 * (1 - mu ** 2))
delta_x_step: float = a_plate / n_elem

a_1 = 3 * b_plate / 8 * d_stiffness / 2
a_2 = (2 * 3.14 ** 4) / b_plate ** 3 * d_stiffness / 2
a_3 = - mu * 3.14 ** 2 / b_plate * d_stiffness / 2
a_4 = (1 - mu) * 3.14 ** 2 / b_plate * d_stiffness / 2
q_1 = b_plate * q_load / 2
# Сбор основной системы уравнений
left_part = np.zeros((n_nodes * 2, n_nodes * 2))
right_part = np.zeros(n_nodes * 2)
left_part_temp = np.zeros((n_nodes * 2, 2))
right_part_temp = np.zeros(2)
for i in range(1, n_nodes - 1, 1):
    print(i)
    x_k_minus_1 = delta_x_step * (i - 1)
    print(x_k_minus_1)
    x_k = delta_x_step * i
    print(x_k)
    x_k_plus_1 = delta_x_step * (i + 1)
    print(x_k_plus_1)
    left_part_temp, right_part_temp = main_equations(n_nodes,
                                                     i + 1,
                                                     x_k_minus_1,
                                                     x_k,
                                                     x_k_plus_1,
                                                     a_1,
                                                     a_2,
                                                     a_3,
                                                     a_4,
                                                     q_1)

    left_part[i - 1] = left_part_temp[0]
    left_part[i - 1 + n_nodes] = left_part_temp[1]
    right_part[i - 1] = right_part_temp[0]
    right_part[i - 1 + n_nodes] = right_part_temp[1]

# print(left_part)
# print(right_part)

# Заполнение уравнений, получающихся из граничных условий
left_part_temp = bound_cond_equations(a_1, a_3, a_4, 0, delta_x_step, 0)

left_part[n_nodes - 2][0] = left_part_temp[0][0]
left_part[n_nodes - 2][1] = left_part_temp[0][1]
left_part[n_nodes - 2][n_nodes] = left_part_temp[0][2]
left_part[n_nodes - 2][n_nodes + 1] = left_part_temp[0][3]

left_part[n_nodes - 1][0] = left_part_temp[1][0]
left_part[n_nodes - 1][1] = left_part_temp[1][1]
left_part[n_nodes - 1][n_nodes] = left_part_temp[1][2]
left_part[n_nodes - 1][n_nodes + 1] = left_part_temp[1][3]

left_part_temp = bound_cond_equations(a_1, a_3, a_4, a_plate - delta_x_step, a_plate, a_plate)

left_part[2 * n_nodes - 2][n_nodes - 2] = left_part_temp[0][0]
left_part[2 * n_nodes - 2][n_nodes - 1] = left_part_temp[0][1]
left_part[2 * n_nodes - 2][2 * n_nodes - 2] = left_part_temp[0][2]
left_part[2 * n_nodes - 2][2 * n_nodes - 1] = left_part_temp[0][3]

left_part[2 * n_nodes - 1][n_nodes - 2] = left_part_temp[1][0]
left_part[2 * n_nodes - 1][n_nodes - 1] = left_part_temp[1][1]
left_part[2 * n_nodes - 1][2 * n_nodes - 2] = left_part_temp[1][2]
left_part[2 * n_nodes - 1][2 * n_nodes - 1] = left_part_temp[1][3]


# print(left_part)
# # print(right_part)
#
vector_w = np.linalg.solve(left_part, right_part)
print(vector_w)
w_middle = vector_w[int(n_elem/2)] * (np.sin(3.14 / 2)) ** 2
print(w_middle)
print(q_load * a_plate * b_plate ** 4 / 384 / E_modulus / (a_plate * h_plate ** 3 / 12))
