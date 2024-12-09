import json

with open("cars.json","r",encoding= "utf-8") as file :
    data = json.load(file)

# Собираем все существующие ID
our_ids = sorted([item["id"] for item in data])
current_id = our_ids[-1:][0]+ 1

count = 0
close = True

def menu():
    print("""
       1: Вывести все записи 
       2: Вывести запись по полю 
       3: Добавить запись 
       4: Удалить запись по полю 
       5: Выйти из программы""")

    #nomer = int(input("Введите номер действия, которое хотите выполнить: "))


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
        index = 0
        idi = int(input("Введите номер машины: "))
        for car in data:
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

                index += 1
        count += 1
    
    
    
def new():
    global count
    name = input(f"Введите имя машины,которую вы хотите добавить,ей будет присвоен id {current_id}: ")  
    manufacturer = input("Введите завод изготовитель: ")  
    is_petrol = input("Введите, заправлена ли машина (да/нет): ")  
    tank_volume = float(input("Введите объем бака машины: "))  

    new_car = {
        'id': current_id,
        'name': name,
        'manufacturer': manufacturer,
        'is_petrol': 'Дизель' if is_petrol == 'д' else 'Бензин', 
        'tank_volume': tank_volume
        }

    data.append(new_car) 
    with open("cars.json", 'w', encoding='utf-8') as output_file: #в переменную output 
        json.dump(data, output_file, ensure_ascii=False, indent=1) # dump куда что раскодировка отступ между
    print("Новая машина добавлена.")
        
    count += 1


def del_car():
    global count
    idd = int(input("Введите номер машины: "))
    flag = False  

    for car in data:
        if idd == car['id']:
            data.remove(car)  
            flag = True  
            break 

        if not flag:
            print("Запись не найдена.")
        else:
            with open("cars.json", 'w', encoding='utf-8') as output_file:
                json.dump(data, output_file, ensure_ascii=False, indent=1)
                print("Машина удалена.")
        count += 1


def leave():
    global count
    global close
    print(f"Программа завершена,выполнено операций: {count}")
    close = False   

def main():
    while close:
        menu()
    
        punkt = int(input("Введите номер действия, которое вы хотите выполнить: "))

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
            print("Такого варианта нет.Введите пункт от 1 до 5!")
            
main()
