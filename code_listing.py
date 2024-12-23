import os

# НАСТРОЙКИ

# Файл, куда будет записываться код, расширение .txt обязательно
output_file_name = 'code_listing.txt'  
# Путь до папки, где будут искаться файлы (подпапки также будут просматриваться)
directory = r''  
# Расширения, которые будут записываться, через запятую
file_extensions = ('.py', '.ui')


# Проверка совпадения расширения файла
def correct_file_extension(filename, file_extensions):
    return f'.{filename.split(".")[-1]}' in file_extensions

# Основная функция
def write_codes(output_file_name, directory, file_extensions):
    print(f'Записываем в {output_file_name} все коды {file_extensions} из {directory}')
    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        # Проходим по всем подпапкам
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                if correct_file_extension(filename, file_extensions): 
                    # Записываем код файла, если корректное расширение
                    file_path = os.path.join(dirpath, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            output_file.write(f'{filename}\n')
                            output_file.write(file.read())
                            output_file.write('\n\n\n')
                        print(f'✓ {file_path}')
                    except UnicodeDecodeError:
                        print(f'Не удалось прочитать файл {file_path}, возможно, некорректная кодировка.')


def main():
    write_codes(output_file_name, directory, file_extensions)

if __name__ == '__main__':
    main()
