def to_hex(num):
    if num < 0:
        raise ValueError("Введите неотрицательное целое число.")
    hex_str = ""
    hex_digits = "0123456789ABCDEF"
    
    if num == 0:
        return "0"
    
    while num > 0:
        remainder = num % 16
        hex_str = hex_digits[remainder] + hex_str
        num //= 16
    
    return hex_str

def main():
    try:
        number = int(input("Введите целое неотрицательное число: "))
        if number < 0:
            print("Ошибка: число должно быть неотрицательным.")
            return
        
        hex_representation = to_hex(number)
        print(f"Шестнадцатеричное представление: {hex_representation}")
        print(f"Проверка с помощью функции hex(): {hex(number)[2:].upper()}")
    
    except ValueError:
        print("Ошибка: введите корректное целое число.")

if __name__ == "__main__":
    main()
