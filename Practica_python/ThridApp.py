import random

class QuickSorter:
#Класс с различными реализациями быстрой сортировки
    
    @staticmethod
    def quicksort_simple(arr):
    #Простая реализация quicksort (не in-place)
        if len(arr) <= 1:
            return arr
        
        # Выбор pivot разными способами:
        # pivot = arr[len(arr) // 2]  # Средний элемент
        # pivot = arr[0]  # Первый элемент
        # pivot = arr[-1]  # Последний элемент
        # pivot = random.choice(arr)  # Случайный элемент
        
        pivot = arr[len(arr) // 2]
        
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return QuickSorter.quicksort_simple(left) + middle + QuickSorter.quicksort_simple(right)
    
    @staticmethod
    def quicksort_inplace(arr, low=0, high=None):
    #Быстрая сортировка на месте
        if high is None:
            high = len(arr) - 1
        
        if low < high:
            # Разные стратегии выбора pivot
            # Можно раскомментировать нужную:
            
            # 1. Всегда последний элемент
            # pivot_index = high
            
            # 2. Случайный элемент (улучшает производительность на отсортированных данных)
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            
            pi = QuickSorter._partition(arr, low, high)
            QuickSorter.quicksort_inplace(arr, low, pi - 1)
            QuickSorter.quicksort_inplace(arr, pi + 1, high)
        
        return arr
    
    @staticmethod
    def _partition(arr, low, high):
    #Вспомогательная функция для разделения
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    @staticmethod
    def quicksort_3way(arr, low=0, high=None):
    #Трехходовая быстрая сортировка (эффективна при многих повторяющихся элементах)
        if high is None:
            high = len(arr) - 1
        
        if low < high:
            lt, gt = QuickSorter._partition_3way(arr, low, high)
            QuickSorter.quicksort_3way(arr, low, lt - 1)
            QuickSorter.quicksort_3way(arr, gt + 1, high)
        
        return arr
    
    @staticmethod
    def _partition_3way(arr, low, high):
    #Разделение для трехходовой сортировки
        pivot = arr[low]
        lt = low      # arr[low..lt-1] < pivot
        gt = high     # arr[gt+1..high] > pivot
        i = low + 1   # arr[lt..i-1] == pivot
        
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        
        return lt, gt
