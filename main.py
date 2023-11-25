# Исходные параметры пластины
a_plate: float = 6  # Длина в направлении x [м]
b_plate: float = 40  # Ширина в направлении y [м]
q_load: float = 0.01  # Распределенная нагрузка [кН/м2]
E_modulus: float = 40000  # Модуль деформации материала [МПа]
mu: float = 0.2  # Коэффициент пуассона
n_elem: int = 3  # Количество элементов, на которые разбивается пластина в направлении x
n_nodes: int = n_elem + 1

