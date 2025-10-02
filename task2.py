import numpy as np
from scipy import integrate as spi

# Функція для інтегрування
def f(x):
    return x**2

# Межі інтегрування
a, b = 0, 2

# Точний результат за допомогою quad
quad_result, quad_error = spi.quad(f, a, b)

# Функція для обчислення інтеграла методом Монте-Карло (метод випадкових точок)
def monte_carlo_integral(func, a, b, num_samples=10000):
    # Генеруємо випадкові точки (x, y) у прямокутнику: [a, b] × [0, f(b)]
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, func(b), num_samples)
    
    # Рахуємо, скільки точок опинилися під кривою y = f(x)
    under_curve = np.sum(y_random < func(x_random))
    
    # Площа під кривою f(x) на проміжку [a, b] обчислюється як:
    # (b - a) * f(b) * (кількість точок під кривою / загальна кількість точок)
    area = (b - a) * func(b) * (under_curve / num_samples)
    return area

# Список різних кількостей точок для порівняння
samples_list = [1000, 10000, 100000, 1000000]

# Вивід результатів у форматі Markdown-таблиці
print("| Кількість точок | Результат Монте-Карло | Абсолютна похибка |")
print("|-----------------|-----------------------|-------------------|")

for n in samples_list:
    mc_val = monte_carlo_integral(f, a, b, n)
    error = abs(mc_val - quad_result)
    print(f"| {n:<15} | {mc_val:<21.6f} | {error:<17.6f} |")

print(f"\nТочний результат (quad, аналітично): {quad_result:.6f} \n")