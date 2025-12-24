# 1
def print_numbers_1_to_n(n):
#Выводит все числа от 1 до nArgs:n: натуральное число

    def helper(current):
        # Базовый случай: если текущее число больше n, завершаем рекурсию
        if current > n:
            return
        # Выводим текущее число
        print(current)
        # Рекурсивный вызов для следующего числа
        helper(current + 1)
    
    # Запускаем рекурсию с начального значения 1
    helper(1)

# 2
def print_numbers_a_to_b(a, b):
#Выводит числа от A до B включительно Args:a: первое числоb: второе число

    def helper(current, target):
        # Выводим текущее число
        print(current)
        
        # Базовый случай: достигли целевого значения
        if current == target:
            return
        
        # Определяем шаг: +1 если идем вверх, -1 если идем вниз
        step = 1 if current < target else -1
        
        # Рекурсивный вызов для следующего числа
        helper(current + step, target)
    
    # Запускаем рекурсию
    helper(a, b)

# 3
def sum_of_digits(n):
#Вычисляет сумму цифр натурального числа Args:n: натуральное числоReturns:Сумма цифр числа
    # Базовый случай: если число меньше 10, это одна цифра
    if n < 10:
        return n
    
    # Рекурсивный случай: 
    # Последняя цифра + сумма цифр остатка числа
    return (n % 10) + sum_of_digits(n // 10)

# 4
def find_smallest_prime_divisor(n, divisor=2):
#Находит наименьший простой делитель числа n Args: n: число для проверки, divisor: текущий делитель, Returns: Наименьший простой делитель

    # Если divisor возведенный в квадрат больше n, то n - простое
    if divisor * divisor > n:
        return n
    
    # Если divisor делит n, возвращаем divisor
    if n % divisor == 0:
        return divisor
    
    # Иначе проверяем следующий делитель
    return find_smallest_prime_divisor(n, divisor + 1)

def print_prime_divisors_simple(n):
#Выводит все простые делители числа в порядке возрастания Args: n: натуральное число > 1

    if n == 1:
        return
    
    # Находим наименьший простой делитель
    p = find_smallest_prime_divisor(n)
    
    # Выводим его
    print(p)
    
    # Убираем все вхождения этого делителя
    while n % p == 0:
        n //= p
    
    # Рекурсивно обрабатываем оставшуюся часть
    print_prime_divisors_simple(n)

    