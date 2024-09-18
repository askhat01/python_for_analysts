def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    while True:
        try:
            number = int(input("Введите число от 0 до 100000: "))
            if number < 0 or number > 100000:
                print("Ошибка: число должно быть в диапазоне от 0 до 100000.")
                continue
            
            if is_prime(number):
                print(f"{number} - простое число.")
            else:
                print(f"{number} - составное число.")
            break
        except ValueError:
            print("Ошибка: введите целое число.")

if __name__ == "__main__":
    main()