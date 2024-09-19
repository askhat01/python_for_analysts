import random

def can_attack(queens):
    rows = set()
    main_diagonals = set()
    anti_diagonals = set()
    
    for x, y in queens:
        if x in rows:
            return False
        rows.add(x)

        if (x - y) in main_diagonals:
            return False
        main_diagonals.add(x - y)

        if (x + y) in anti_diagonals:
            return False
        anti_diagonals.add(x + y)

    return True

def random_queen_placements(n=8):
    successful_placements = []
    attempts = 0

    while len(successful_placements) < 4 and attempts < 1000:
        # Генерируем случайные позиции для 8 ферзей
        columns = random.sample(range(1, n + 1), n)
        queens = [(row + 1, columns[row]) for row in range(n)]
        
        if can_attack(queens):
            successful_placements.append(queens)
        
        attempts += 1

    return successful_placements

# Основная программа
if __name__ == "__main__":
    successful_arrangements = random_queen_placements()
    print("Успешные расстановки ферзей:")
    for arrangement in successful_arrangements:
        print(arrangement)
