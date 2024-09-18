import re
from collections import Counter

def count_words(text):
    # Удаляем знаки препинания и переводим текст в нижний регистр
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Разбиваем текст на слова
    words = cleaned_text.split()
    
    # Подсчитываем количество вхождений слов
    word_counts = Counter(words)
    
    # Получаем 10 самых распространенных слов
    most_common_words = word_counts.most_common(10)
    
    return most_common_words

# Пример текста из статьи о Искусственном интеллекте
text = """
Искусственный интеллект (ИИ) — это область информатики, 
которая занимается созданием систем, способных выполнять задачи, 
требующие человеческого интеллекта. К таким задачам относятся 
распознавание речи, понимание естественного языка, 
принятие решений и обучение. ИИ используется в различных областях, 
включая медицину, финансы, транспорт и многих других.
"""

if __name__ == "__main__":
    common_words = count_words(text)
    print("10 самых частых слов:")
    for word, count in common_words:
        print(f"{word}: {count}")
