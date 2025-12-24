def max_lectures(n, requests):
   
   # Алгоритм жадного выбора по времени окончания:
    #1. Сортируем заявки по времени окончания (fi)
    #2. Берем первую заявку (с самым ранним окончанием)
    #3. Далее выбираем следующую заявку, которая начинается не раньше окончания предыдущей

    # Сортируем заявки по времени окончания
    requests.sort(key=lambda x: x[1])
    
    count = 0
    last_end = 0  # Время окончания последней выбранной лекции
    
    for start, end in requests:
        if start >= last_end:  # Лекция может начаться после окончания предыдущей
            count += 1
            last_end = end
    
    return count


def max_boxes(n, boxes):
    # Оптимизированный алгоритм с использованием динамического программирования
    # для больших значений n (до 10^5)

    # Сортируем коробки по (ci + wi)
    boxes.sort(key=lambda x: x[0] + x[1])
    
    # Динамическое программирование: dp[i] - минимальный вес для башни из i коробок
    INF = float('inf')
    dp = [INF] * (n + 1)
    dp[0] = 0  # Башня из 0 коробок имеет вес 0
    
    max_possible = 0
    
    for weight, capacity in boxes:
        # Обновляем dp снизу вверх, чтобы не использовать коробку дважды
        for i in range(max_possible, -1, -1):
            if dp[i] <= capacity:  # Можем положить коробку сверху
                dp[i + 1] = min(dp[i + 1], dp[i] + weight)
                max_possible = max(max_possible, i + 1)
    
    return max_possible