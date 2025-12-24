# Импортируем модуль random для генерации случайных чисел
import random
import heapq

import FirstApp
import SecondApp
import ThridApp
import FourthApp
import FifthApp
import SixApp
import SevenApp

# Основной блок программы, который выполняется при запуске скрипта
if __name__ == "__main__":

    # ВЫПОЛНЕНИЕ ПЕРВОГО ЗАДАНИЯ 

    # Генерация массива из 15 случайных целых чисел в диапазоне от 2 до 103
    # Цикл выполняется 15 раз, _ - временная переменная, которая не используется
    array = [random.randint(2, 103) for _ in range(15)]
    # Выводим исходный массив на экран
    print("mass:", array)

    # Сортируем копию массива по возрастанию (чтобы не изменять исходный массив)
    sorted_array_asc = FirstApp.selection_sort_asc(array.copy())
    # Сортируем копию массива по убыванию
    sorted_array_desc = FirstApp.selection_sort_desc(array.copy())

    # Выводим отсортированный по возрастанию массив
    print("Sort UP mass:", sorted_array_asc)
    # Выводим отсортированный по убыванию массив
    print("Sort DOWN mass:", sorted_array_desc)

    # Создаем список телефонных номеров в формате строк с дефисами
    phone_numbers = [
    "23-45-67",  # Первый телефонный номер
    "12-34-56",  # Второй телефонный номер
    "98-76-54",  # Третий телефонный номер
    "11-22-33",  # Четвертый телефонный номер
    "55-66-77",  # Пятый телефонный номер
    "01-23-45"   # Шестой телефонный номер
    ]

    # Выводим заголовок перед списком телефонных номеров
    print("\nList numbers:")
    # Проходим по всем телефонным номерам в списке
    for phone in phone_numbers:
        # Выводим каждый телефонный номер на отдельной строке
        print(phone)

    # Сортируем копию списка телефонных номеров по возрастанию
    sorted_phones = FirstApp.selection_sort_phones(phone_numbers.copy())

    # Выводим заголовок перед отсортированным списком телефонных номеров
    print("\nSort list numbers:")
    # Проходим по всем отсортированным телефонным номерам
    for phone in sorted_phones:
        # Выводим каждый отсортированный телефонный номер на отдельной строке
        print(phone)

    # ВЫПОЛНЕНИЕ ВТОРОГО ЗАДАНИЯ 
    n = int(input("Write Natural Num (>1): "))

    print(f"Num at 1 to {n}:")
    SecondApp.print_numbers_1_to_n(n)

    result = SecondApp.sum_of_digits(n)
    print(f"Sum nums in {n} = {result}")

    if n > 1:
        print(f"Prime divisors {n}:")
        SecondApp.print_prime_divisors_simple(n)


    a = int(input("Write num A: "))
    b = int(input("Write num B: "))
    print(f"Nums at {a} to {b}:")
    SecondApp.print_numbers_a_to_b(a, b)

    # ВЫПОЛНЕНИЕ ТРЕТЬЕГО ЗАДАНИЯ 

    print("=" * 60)
    print("DEMONSTRATION FAST SORT")
    print("=" * 60)


    # 1. Test with 1000 numbers
    print("\n1. Sorting a sequence of 1000 numbers:")
    seq = [random.randint(-1000, 1000) for _ in range(1000)]
    sorted_seq = ThridApp.QuickSorter.quicksort_simple(seq.copy())
    print(f"   First 5 elements: {sorted_seq[:5]}")
    print(f"   Last 5 elements: {sorted_seq[-5:]}")
    print(f"   Sorting correctness: {sorted_seq == sorted(seq)}")

    # 2. Test with range 50-100
    print("\n2. Sorting an array in range 50-100:")
    arr = [random.randint(50, 100) for _ in range(20)]
    sorted_arr = ThridApp.QuickSorter.quicksort_inplace(arr.copy())
    print(f"   Original: {arr}")
    print(f"   Sorted: {sorted_arr}")

    # 3. Test with 2D array
    print("\n3. Sorting a 2D array by the first column:")
    matrix = [[random.randint(5, 61) for _ in range(3)] for _ in range(5)]
    print("   Original array:")
    for row in matrix:
        print(f"   {row}")

    # Sorting by first column
    sorted_matrix = sorted(matrix, key=lambda x: x[0]) 
    print("\n   Sorted by first column:")
    for row in sorted_matrix:
        print(f"   {row}")

    # 4. Test with students
    print("\n4. Sorting students alphabetically:")
    students = [
        "Ivanov Ivan", "Petrov Petr", "Sidorov Alexey",
        "Abramov Mikhail", "Kozlova Anna"
    ]
    sorted_students = sorted(students)  # Built-in sorting
    print("   Sorted list:")
    for student in sorted_students:
        print(f"   {student}")

    # ВЫПОЛНЕНИЕ ЧЕТВЕРТОГО ЗАДАНИЯ 

    FourthApp.process_hash_table_sequence()

    # ВЫПОЛНЕНИЕ ПЯТОГО ЗАДАНИЯ

    print("="*50)
    print("SEARCH SHOTEST MOVING ON LABIRINT")
    print("ALG (BFS)")
    print("="*50)
    
    # 1. Строим граф лабиринта
    maze_graph = FifthApp.build_maze_graph()
    
    # 2. Визуализируем граф
    FifthApp.visualize_graph(maze_graph)
    
    # 3. Задаем начальную и конечную точки
    start_room = 'A'
    end_room = 'J'
        
    # 4. Выполняем BFS для поиска кратчайшего пути
    shortest_path = FifthApp.bfs_shortest_path(maze_graph, start_room, end_room)
    
    # 5. Выводим результат
    print("\n3. RESULT:")
    print("-" * 30)
    
    if shortest_path:
        print(f"SHORTEST!")
        print(f"DLINNA: {len(shortest_path) - 1} STEPS")
        print(f"PUTb: {' -> '.join(shortest_path)}")
        
        # Дополнительная информация
        print(f"\nDITAILS:")
        for i in range(len(shortest_path) - 1):
            print(f"  STEP {i+1}: {shortest_path[i]} -> {shortest_path[i+1]}")
    else:
        print(f" '{start_room}' TO '{end_room}' NOT EXIST!")
    

    # ВЫПОЛНЕНИЕ ШЕСТОГО ЗАДАНИЯ

    # Предзаданные входные данные для задачи 1
    n = 5
    S = 1
    F = 4

    # Матрица смежности (5x5)
    graph_matrix = [
        [0, 10, -1, 30, 100],
        [-1, 0, 50, -1, -1],
        [-1, -1, 0, -1, 10],
        [-1, -1, 20, 0, 60],
        [-1, -1, -1, -1, 0]
    ]

    # Приводим к 0-индексации
    s = S - 1
    f = F - 1

    # Выполнение алгоритма
    result = SixApp.dijkstra(n, s, f, graph_matrix)
    print(f"Shortest at {S} to {F}: {result}")


    # Предзаданные входные данные для задачи 2
    n = 5
    prices = [10, 20, 5, 15, 30]  # Стоимость бензина в каждом городе
    m = 5  # Количество дорог

    # Дороги (каждая дорога соединяет два города)
    roads_data = [
        (1, 2),
        (1, 3),
        (2, 4),
        (3, 4),
        (4, 5)
    ]

    # Преобразуем дороги к 0-индексации
    roads = [(u - 1, v - 1) for u, v in roads_data]

    # Вычисление результата
    result = SixApp.min_cost_path(n, prices, roads)
    print(f"min price at first city to {n}: {result}")

    # ВЫПОЛНЕНИЕ СЕДЬМОГО ЗАДАНИЯ


    # Предзаданные входные данные для задачи 1
    n1 = 5
    requests1 = [
        [1, 3],
        [2, 5],
        [4, 6],
        [6, 7],
        [5, 8]
    ]

    # Выполнение
    result1 = SevenApp.max_lectures(n1, requests1)
    print(f"Max count zayavok = {result1}")

    # Предзаданные входные данные для задачи 2
    n2 = 4
    boxes2 = [
        [10, 100],   # Вес 10, выдерживает 100
        [20, 50],    # Вес 20, выдерживает 50
        [30, 60],    # Вес 30, выдерживает 60
        [40, 40]     # Вес 40, выдерживает 40
    ]

    # Выполнение
    result2 = SevenApp.max_boxes(n2, boxes2)
    print(f"MAX boxes = {result2}")