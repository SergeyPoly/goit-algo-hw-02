def check_brackets(string: str) -> str:
    # Словник для зіставлення дужок
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    
    # Стек для відстеження дужок
    stack = []
    
    for char in string:
        # Якщо символ - це відкриваюча дужка, додаємо його в стек
        if char in matching_brackets.values():
            stack.append(char)
        # Якщо символ - це закриваюча дужка
        elif char in matching_brackets.keys():
            # Перевіряємо, чи є відповідна відкриваюча дужка у стеку
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()  # Видаляємо зі стеку, якщо знайшли пару
            else:
                return "Несиметричні розділювачі або різні види дужок у парі"
    
    # Якщо стек порожній, дужки симетричні
    if not stack:
        return "Розділювачі симетричні"
    else:
        return "Несиметричні розділювачі"

test_strings = [
    "( ) { [ ] ( ) ( ) { } }",
    "( ( ( )",
    "( }",
    "{ [ ( ) ] }",
    "{ [ ( ] ) }"
]

for string in test_strings:
    print(f"'{string}' -> {check_brackets(string)}")