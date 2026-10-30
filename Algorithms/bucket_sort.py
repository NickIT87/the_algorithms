def bucket_sort(arr):
    n = len(arr)

    buckets = [[] for _ in range(n)]

    # Распределение по корзинам
    for num in arr:
        index = int(num * n)
        if index == n:
            index = n - 1
        buckets[index].append(num)

    # Сортировка каждой корзины
    for bucket in buckets:
        bucket.sort()

    # Объединение корзин
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result


arr = [0.42, 0.32, 0.75, 0.12, 0.89, 0.55, 0.23]

print(bucket_sort(arr))