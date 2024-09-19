import os
import json
import csv
import pickle

def get_directory_info(path):
    directory_info = []

    for root, dirs, files in os.walk(path):
        total_size = 0

        # Обработка файлов
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size
            directory_info.append({
                'name': file,
                'path': file_path,
                'type': 'file',
                'size': file_size,
                'parent': root
            })

        # Обработка директорий
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            directory_info.append({
                'name': dir,
                'path': dir_path,
                'type': 'directory',
                'size': total_size,  # Здесь указываем сумму размеров всех файлов
                'parent': root
            })

    return directory_info

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, filename):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

def process_directory(path):
    directory_info = get_directory_info(path)

    # Сохранение в различные форматы
    save_to_json(directory_info, 'directory_info.json')
    save_to_csv(directory_info, 'directory_info.csv')
    save_to_pickle(directory_info, 'directory_info.pkl')

# Пример использования:
# process_directory('/path/to/directory')
