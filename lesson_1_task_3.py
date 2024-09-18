from random import randint

def main():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    attempts = 10

    print("Я загадал число от 0 до 1000. Угадайте его за 10 попыток!")

    for attempt in range(attempts):
        try:
            guess = int(input(f"Попытка {attempt + 1}: Введите ваше число: "))
            
            if guess < LOWER_LIMIT or guess > UPPER_LIMIT:
                print(f"Ошибка: число должно быть в диапазоне от {LOWER_LIMIT} до {UPPER_LIMIT}.")
                continue
            
            if guess < secret_number:
                print("Меньше. Попробуйте снова.")
            elif guess > secret_number:
                print("Больше. Попробуйте снова.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempt + 1} попыток!")
                break
        except ValueError:
            print("Ошибка: введите целое число.")
    
    else:
        print(f"Вы исчерпали попытки. Загаданное число было {secret_number}.")

if __name__ == "__main__":
    main()