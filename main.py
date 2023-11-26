from Phi_function import phi_function
from Linear_system_solver_for_coefficients import calc_coefficients
from Phi_derivative_x import phi_derivative_x
from Phi_derivative_w import phi_derivative_w
from sympy import symbols

# Исходные параметры пластины
a_plate: float = 6  # Длина в направлении x [м]
b_plate: float = 40  # Ширина в направлении y [м]
q_load: float = 0.01  # Распределенная нагрузка [кН/м2]
E_modulus: float = 40000  # Модуль деформации материала [МПа]
mu: float = 0.2  # Коэффициент пуассона
n_elem: int = 3  # Количество элементов, на которые разбивается пластина в направлении x
n_nodes: int = n_elem + 1

w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x = symbols('w_k_1 dw_dx_k_1 w_k dw_dx_k x_k_1 x_k x')

print(phi_derivative_x(w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k))
print(phi_derivative_w(w_k_1, dw_dx_k_1, w_k, dw_dx_k, x_k_1, x_k, x))


