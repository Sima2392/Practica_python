def process_hash_table_sequence(input_filename='input.txt', output_filename='output.txt'):
#Решение задачи с использованием хэш-таблицы (словаря Python) Чтение из входного файла, запись результата в выходной файл
    try:
        # 1. Чтение данных из входного файла
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            data = input_file.read().strip().split()
        
        # 2. Инициализация хэш-таблицы (словаря)
        # Ключ: число, Значение: количество вхождений
        hash_table = {}
        
        # 3. Обработка последовательности чисел
        for item in data:
            num = int(item)
            
            if num > 0:
                # Добавляем положительное число
                hash_table[num] = hash_table.get(num, 0) + 1
                
            elif num < 0:
                # Удаляем противоположное число
                opposite = -num
                if opposite in hash_table:
                    hash_table[opposite] -= 1
                    if hash_table[opposite] <= 0:
                        del hash_table[opposite]
                        
            else:  # num == 0
                # 4. Встретили 0 - формируем результат
                break
        
        # 5. Сортировка чисел по возрастанию
        sorted_numbers = sorted(hash_table.keys())
        
        # 6. Формирование результата ТОЛЬКО ИЗ УНИКАЛЬНЫХ ЗНАЧЕНИЙ
        # Каждое число добавляется только 1 раз, независимо от количества вхождений
        result_list = []
        for number in sorted_numbers:
            # Добавляем число только один раз (даже если count > 1)
            result_list.append(str(number))

        
        # 7. Запись результата в выходной файл
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(' '.join(result_list))
            
        print(f"Result successful read {output_filename}")
        return True
        
    except FileNotFoundError:
        print(f"Exception: file {input_filename} not found")
        print(f"Create {input_filename} in the folder of programm")
        return False
    except ValueError as e:
        print(f"Exception in data: {e}")
        return False
    except Exception as e:
        print(f"not found Exception: {e}")
        return False