def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример использования
if __name__ == "__main__":
    fib_gen = fibonacci_generator()
    
    # Вывод первых 10 чисел Фибоначчи
    for _ in range(10):
        print(next(fib_gen))
