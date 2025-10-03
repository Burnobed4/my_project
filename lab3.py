#Задание 1
squares = [x**2 for x in range(1, 11)]
print("1. Квадраты чисел:", squares)

#Задание 2
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print("2. Чётные числа:", even_numbers)

#Задание 3
words = ["python", "Java", "c++", "Rust", "go"]
f_words = [word.upper() for word in words if len(word) > 3]
print("3. Отфильтрованные слова:", f_words)

#Задание 4
class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current < 1:
            raise StopIteration
        return self.current


print("4. Вывод:")
for x in Countdown(5):
    print(x, end=" ")

#Задание 5
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("\n5. Числа Фибоначчи:")
for num in fibonacci(5):
    print(num, end=" ")

#Задание 6

from decimal import Decimal, ROUND_HALF_UP


def deposit_calculator():
    print("\n6.")
    # Ввод данных
    initial_amount = Decimal(input("Введите начальную сумму вклада (рубли.копейки): "))
    interest_rate = Decimal(input("Введите годовую процентную ставку (например, 7.5): "))
    years = Decimal(input("Введите срок вклада в годах: "))

    # Расчет по формуле ежемесячной капитализации
    # S = P * (1 + r/(12*100))^(12*t)
    monthly_rate = interest_rate / (12 * 100)
    months = 12 * years
    final_amount = initial_amount * (1 + monthly_rate) ** months

    # Округление до копеек
    final_amount = final_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    # Расчет прибыли
    profit = final_amount - initial_amount

    # Вывод результатов
    print(f"\nРезультаты расчета:")
    print(f"Начальная сумма: {initial_amount} руб.")
    print(f"Итоговая сумма: {final_amount} руб.")
    print(f"Общая прибыль: {profit} руб.")

# Запуск калькулятора
deposit_calculator()

#Задание 7
from fractions import Fraction
print("7. Работа с дробями:")
a = Fraction(3, 4)
b = Fraction(5, 6)

print(f"Дробь A = {a}")
print(f"Дробь B = {b}")
print(f"Сложение: {a} + {b} = {a + b}")
print(f"Вычитание: {a} - {b} = {a - b}")
print(f"Умножение: {a} * {b} = {a * b}")
print(f"Деление: {a} / {b} = {a / b}")

#Задание 8
from datetime import datetime
print("8. Текущая дата и время:")
now = datetime.now()
print(f"Текущая дата и время: {now}")
print(f"Текущая дата: {now.date()}")
print(f"Текущее время: {now.time()}")

#Задание 9
from datetime import date
print("9. Разница дат:")
birthday = date(2005, 8, 15)
today = date.today()

# Сколько дней прошло с рождения
days_passed = (today - birthday).days

# Следующий день рождения
next_birthday = date(today.year, birthday.month, birthday.day)
if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_to_next_birthday = (next_birthday - today).days

print(f"Дата рождения: {birthday}")
print(f"Сегодня: {today}")
print(f"Дней прошло с рождения: {days_passed}")
print(f"Дней до следующего дня рождения: {days_to_next_birthday}")

#Задание 10
print("10. Datatime:")
now = datetime.now()

months = {
    1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
    5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
    9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
}

result = f"Сегодня {now.day} {months[now.month]} {now.year} года, время: {now.strftime('%H:%M')}"
print(result)