import os
import shutil



def parse_input(user_input):
    cmd = user_input
    cmd = cmd.strip().lower()
    return cmd


def copy_files(source_dir, dest_dir='dist'):
        """
        Рекурсивно копіює файли з source_dir до dest_dir, сортуючи їх по піддиректоріях, заснованих на їхніх розширеннях.
        """
        try:
            # Перевірка наявності директорії призначення; створення, якщо не існує
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
        
            for item in os.listdir(source_dir):
                full_item_path = os.path.join(source_dir, item)
                if os.path.isdir(full_item_path):
                    # Рекурсивний виклик для піддиректорій
                    copy_files(full_item_path, dest_dir)
                else:
                    # Визначення піддиректорії для копіювання на основі розширення файла
                    file_extension = os.path.splitext(item)[1][1:] # Видаляємо крапку з розширення
                    extension_dir = os.path.join(dest_dir, file_extension)
                    if not os.path.exists(extension_dir):
                        os.makedirs(extension_dir)
                
                    dest_file_path = os.path.join(extension_dir, item)
                    shutil.copy2(full_item_path, dest_file_path)
                    print(f"Файл {full_item_path} було скопійовано до {dest_file_path}")
        except Exception as e:
            print(f"Помилка: {e}")


def main():
    print("Ласкаво просимо до програми копіювання файлів!")

    while True:
        user_input = input("Введіть команду: 'start' - почати, 'exit' - вийти: ")
        command = parse_input(user_input)

            
        if command == "exit":
            print("До побачення!")
            break
        elif command == "start":
            user_input = input("Введіть шлях до вихідної директорії та за бажанням до директорії призначення: ").split()
        
            if not user_input:
                print("Не вірно вказано шлях")
            elif len(user_input) < 2:
                copy_files(user_input[0], dest_dir='dist')
            else:    
                copy_files(user_input[0], user_input[1])
        else:
            print("Не вірна команда!")





if __name__ == "__main__":
    main()
