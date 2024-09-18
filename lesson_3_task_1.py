from collections import Counter

def find_duplicates(input_list):
    # Подсчет вхождений элементов
    counts = Counter(input_list)
    # Получение элементов, которые повторяются более одного раза
    duplicates = [item for item, count in counts.items() if count > 1]
    return duplicates

# Пример использования
if __name__ == "__main__":
    input_list = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]
    result = find_duplicates(input_list)
    print("Дублирующиеся элементы:", result)
