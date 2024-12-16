import json

# Открываем файл и загружаем данные
with open("cars.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Собираем все существующие ID
our_ids = sorted([item["id"] for item in data])
current_id = our_ids[-1:][0] + 1

count = 0
close = True

def menu():
    print("""
       1: Вывести все записи 
       2: Вывести запись по полю 
       3: Добавить запись 
       4: Удалить запись по полю 
       5: Выйти из программы""")

def get_int_input(prompt):
    """Функция для ввода целого числа с проверкой"""
    while True:
        user_input = input(prompt)
        if user_input.isdigit():  # Проверка на целое число
            return int(user_input)
        else:
            print("Введите корректное число.")

def get_float_input(prompt):
    """Функция для ввода числа с плавающей запятой"""
    while True:
        try:
            return float(input(prompt))  # Попытка преобразовать ввод в число с плавающей запятой
        except ValueError:
            print("Введите корректное число с плавающей запятой.")

def get_yes_no_input(prompt):
    """Функция для ввода ответа да/нет"""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'да':
            return True
        elif user_input == 'нет':
            return False
        else:
            print("Введите 'да' или 'нет'.")

def out_info():
    global count
    for car in data:
        print(f"""
        Код: {car['id']}, 
        Имя: {car['name']},                       
        Фабрика: {car['manufacturer']}, 
        Заправлена: {car['is_petrol']},    
        Объем бака: {car['tank_volume']} 
        """)
    count += 1

def out_index():
    global count
    idi = get_int_input("Введите номер машины: ")
    for index, car in enumerate(data):
        if idi == car['id']:
            print(f"""
            Код: {car['id']}, 
            Имя: {car['name']},                       
            Фабрика: {car['manufacturer']}, 
            Заправлена: {car['is_petrol']},    
            Объем бака: {car['tank_volume']}
            Индекс в списке: {index}
            """) 
            break
    else:
        print("Запись о машине не найдена.")
    count += 1

def new():
    global count
    name = input(f"Введите имя машины, которую вы хотите добавить, ей будет присвоен id {current_id}: ")  
    manufacturer = input("Введите завод изготовитель: ")  
    is_petrol = get_yes_no_input("Введите, заправлена ли машина (да/нет): ")  
    tank_volume = get_float_input("Введите объем бака машины: ")

    new_car = {
        'id': current_id,
        'name': name,
        'manufacturer': manufacturer,
        'is_petrol': 'Дизель' if not is_petrol else 'Бензин', 
        'tank_volume': tank_volume
    }

    data.append(new_car) 
    with open("cars.json", 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=1)
    print("Новая машина добавлена.")
    count += 1

def del_car():
    global count
    idd = get_int_input("Введите номер машины: ")
    for car in data:
        if idd == car['id']:
            data.remove(car)  
            with open("cars.json", 'w', encoding='utf-8') as output_file:
                json.dump(data, output_file, ensure_ascii=False, indent=1)
            print("Машина удалена.")
            break
    else:
        print("Запись не найдена.")
    count += 1

def leave():
    global count
    global close
    print(f"Программа завершена, выполнено операций: {count}")
    close = False

def main():
    while close:
        menu()
        punkt = get_int_input("Введите номер действия, которое вы хотите выполнить: ")

        if punkt == 1:
            out_info()

        elif punkt == 2:
            out_index()

        elif punkt == 3:
            new()

        elif punkt == 4:
            del_car()

        elif punkt == 5:
            leave()
        else:
            print("Такого варианта нет. Введите пункт от 1 до 5!")

main()
