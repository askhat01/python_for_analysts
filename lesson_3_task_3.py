def find_combinations(items, max_weight, current_combination=None, start_index=0):
    if current_combination is None:
        current_combination = []
    
    total_weight = sum(items[item] for item in current_combination)
    
    # Если текущая комбинация превышает грузоподъемность, выходим
    if total_weight > max_weight:
        return []

    # Если текущая комбинация в пределах грузоподъемности, добавляем её в результаты
    valid_combinations = []
    if total_weight <= max_weight:
        valid_combinations.append(current_combination)

    # Пробуем добавить каждую вещь в рюкзак
    for i in range(start_index, len(items)):
        item = list(items.keys())[i]
        valid_combinations += find_combinations(items, max_weight, current_combination + [item], i + 1)

    return valid_combinations

# Словарь с вещами и их массой
items = {
    "палатка": 5,
    "спальный мешок": 2,
    "каримат": 1,
    "еда": 3,
    "вода": 1,
    "фляга": 0.5,
    "первый аптечка": 1.5,
    "фонарик": 0.5
}

# Максимальная грузоподъемность рюкзака
max_weight = 7

if __name__ == "__main__":
    combinations = find_combinations(items, max_weight)
    print("Все возможные варианты комплектации рюкзака:")
    for combo in combinations:
        print(combo)
