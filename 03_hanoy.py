def hanoi(n: int, start: str, transitive: str, target: str, state: dict[list[int]]):
    if n > 0:
        # Рекурсивно переміщуємо n-1 дисків з початкової башти на проміжну
        hanoi(n - 1, start, target, transitive, state)
        
        # Переміщуємо найбільший диск з початкової башти на цільову
        disk = state[start].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {start} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
        
        # Рекурсивно переміщуємо n-1 дисків з проміжної башти на цільову
        hanoi(n - 1, transitive, start, target, state)

def solve_hanoi(n):
    state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {state}")
    hanoi(n, 'A', 'B', 'C', state)
    print(f"Кінцевий стан: {state}")

solve_hanoi(4)