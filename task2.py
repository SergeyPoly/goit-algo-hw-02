from collections import deque

def is_palindrome(s: str) -> bool:
    # Переводимо рядок у нижній регістр і видаляємо всі пробіли а також інші символи, крім букв
    cleaned_string = ''.join(filter(str.isalnum, s)).lower()

    # Якщо рядок містить менше двох символів, він автоматично є паліндромом
    if len(cleaned_string) < 2:
        return True

    # Створюємо двосторонню чергу (deque) і заповнюємо її символами рядка
    deque_str = deque(cleaned_string)

    # Порівнюємо символи з обох кінців черги, поки вона не спорожніє
    while len(deque_str) > 1:
        if deque_str.popleft() != deque_str.pop():
            return False # Якщо не співпадають - це не паліндром

    return True # Якщо всі символи співпали

test_strings = [
    "A man a plan a canal Panama",
    "A man, a plan, a canal: Panama",
    "race car",
    "race a car",
    "Hello, World!",
    "Able was I saw elba",
    " A"
]

for string in test_strings:
    print(f"'{string}' -> Паліндром: {is_palindrome(string)}")