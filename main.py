import json

with open("cars.json","r",encoding= "utf-8") as file :
    data = json.load(file)

# Собираем все существующие ID
our_ids = sorted([item["id"] for item in data])
current_id = our_ids[-1:][0]+ 1

#current_id = our_ids[:-1]+1


count = 0

while True:
    print("""
       1: Вывести все записи n
       2: Вывести запись по полю n
       3: Добавить запись n
       4: Удалить запись по полю n
       5: Выйти из программы""")

    nomer = int(input("Введите номер действия, которое хотите выполнить: "))


    if nomer == 1:
        for car in data:
            print(f"""
            Код: {car['id']}, 
            Имя: {car['name']},                       
            Фабрика: {car['manufacturer']}, 
            Заправлена: {car['is_petrol']},    
            Объем бака: {car['tank_volume']} 
            """)
        count += 1

    elif nomer == 2:
        index = 0
        idi = int(input("Введите номер машины: "))
        flag = False  
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
                flag = True  
                break  
            index += 1
        count += 1
        if not flag:
            print("Запись о машине не найдена.")
    
    
    
    elif nomer == 3:
        #idn = int(input("Введите номер машины: "))
       
        #exists = False
        #for car in data:
            #if car['id'] == current_id:
                #exists = True
                #break
        
        #if exists:
            #print("Машина с таким номером уже существует.")
        #else:
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


    elif nomer == 4:
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


    elif nomer == 5:
        print(f"Программа завершена,выполнено операций: {count}")
        break  


    else:
        print("Такого варианта нет,пожалуйста, выберите пункт 1-5.")


    
    

