from queue import Queue
import random
import datetime
import time

# Створюємо чергу заявок та стартовий id заявки
request_queue = Queue()
request_id = 1

def generate_request():
    # Формування заявки
    global request_id
    new_request = {
        'id': request_id,
        'data': random.randrange(100),
        'date': datetime.datetime.now()
    }
    # Додаємо заявку до черги
    request_queue.put(new_request)  
    request_id += 1

    return new_request


def process_request():
    # Перевіряємо, чи є заявки у черзі
    if request_queue.empty():
        return None
        
    # Видаляємо першу заявку з черги
    current_request = request_queue.get() 
    time.sleep(random.uniform(0.5, 2))  # Імітація часу обробки

    return current_request
        

def main():
    print("\nСистема обробки заявок запущена. Натисніть Ctrl+C для завершення.")
    try:
        while True:
            user_choice = input("\nБудь ласка, оберіть опцію: \n[1] Додати заявку, [2] Обробити заявку, [3] Завершити програму.\n")
            if user_choice == "1":
                new_request = generate_request()
                print(f"\nЗаявка №{new_request['id']} додана до черги.")

            elif user_choice == "2":
                processed_request = process_request()
                if processed_request:
                    print(f"\nЗаявка №{processed_request['id']} успішно оброблена!")
                else:
                    print("\nЧерга пуста. Немає заявок для обробки.")

            elif user_choice == "3":
                print("\nПрограма завершена.")
                break

            else:
                print("\nНевірний вибір. Введіть 1, 2 або 3.")

    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")

if __name__ == '__main__':
    main()