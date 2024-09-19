def can_attack(queens):
    # queens - список координат ферзей (x, y)
    rows = set()
    main_diagonals = set()
    anti_diagonals = set()
    
    for x, y in queens:
        # Проверяем, есть ли ферзь в той же строке
        if x in rows:
            return False
        rows.add(x)

        # Проверяем главную диагональ (x - y)
        if (x - y) in main_diagonals:
            return False
        main_diagonals.add(x - y)

        # Проверяем побочную диагональ (x + y)
        if (x + y) in anti_diagonals:
            return False
        anti_diagonals.add(x + y)

    return True

# Основная программа
if __name__ == "__main__":
    # Задаем позиции ферзей (пример: [(1, 1), (2, 5), ...])
    queens_positions = [
        (1, 1),
        (2, 5),
        (3, 8),
        (4, 6),
        (5, 2),
        (6, 4),
        (7, 3),
        (8, 7)
    ]

    if can_attack(queens_positions):
        print("Истина: ферзи не бьют друг друга.")
    else:
        print("Ложь: ферзи бьют друг друга.")
