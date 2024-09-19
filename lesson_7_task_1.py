import os

def rename_files(directory, base_name, num_digits, old_ext, new_ext, name_range):
    # Проходим по файлам в указанном каталоге
    files = [f for f in os.listdir(directory) if f.endswith(old_ext)]
    
    for count, filename in enumerate(files, start=1):
        # Получаем оригинальное имя файла без расширения
        original_name = os.path.splitext(filename)[0]
        
        # Извлекаем диапазон символов из оригинального имени
        if len(original_name) < name_range[1]:
            print(f"Имя файла {filename} слишком короткое для заданного диапазона.")
            continue
        
        # Извлекаем нужную часть оригинального имени
        sliced_name = original_name[name_range[0]-1:name_range[1]]  # Индексация с 0
        
        # Формируем новое имя файла
        new_file_name = f"{sliced_name}{base_name}{str(count).zfill(num_digits)}.{new_ext}"
        
        # Полные пути к старому и новому файлам
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_file_name)
        
        # Переименовываем файл
        os.rename(old_file_path, new_file_path)
        print(f"Переименован: {old_file_path} -> {new_file_path}")

# Пример использования
if __name__ == "__main__":
    rename_files(
        directory='path/to/directory',  # Укажите путь к каталогу
        base_name='newname',             # Желаемое конечное имя файлов
        num_digits=3,                    # Количество цифр в порядковом номере
        old_ext='.txt',                  # Исходное расширение файла
        new_ext='txt',                   # Конечное расширение файла
        name_range=[3, 6]                # Диапазон сохраняемого оригинального имени
    )
