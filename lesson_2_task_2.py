from fractions import Fraction

def main():
    # Ввод двух дробей
    frac1 = input("Введите первую дробь (a/b): ")
    frac2 = input("Введите вторую дробь (a/b): ")
    
    # Преобразование строк во фракции
    fraction1 = Fraction(frac1)
    fraction2 = Fraction(frac2)
    
    # Вычисление суммы и произведения дробей
    sum_frac = fraction1 + fraction2
    product_frac = fraction1 * fraction2
    
    # Вывод результатов
    print(f"Сумма дробей: {sum_frac}")
    print(f"Произведение дробей: {product_frac}")

if __name__ == "__main__":
    main()
