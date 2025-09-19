import random


#  ЦИКЛЫ


# 1. Таблица умножения
print("\n1. Таблица умножения:")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:4}", end="")
    print()

# 2. Сумма нечётных чисел
sum_odd = sum(i for i in range(1, 101) if i % 2 != 0)
print(f"\n2. Сумма нечётных чисел от 1 до 100: {sum_odd}")

# 3. Делители числа
num = int(input("\n3. Введите число: "))
dividers = [i for i in range(1, num + 1) if num % i == 0]
print(f"Делители числа {num}: {dividers}")

# 4. Факториал
n = int(input("\n4. Введите число для факториала: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факториал {n}! = {factorial}")

# 5. Последовательность Фибоначчи
n = int(input("\n5. Введите длину последовательности Фибоначчи: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(f"Последовательность Фибоначчи: {fib[:n]}")


#  СПИСКИ


# Генерация случайного списка
numbers = [random.randint(-59, 50) for _ in range(10)]
print(f"Сгенерированный список: {numbers}")

# 1. Чётные элементы
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"\n1. Чётные элементы: {even_numbers}")

# 2. Максимум и минимум
print(f"\n2. Максимум: {max(numbers)}, Минимум: {min(numbers)}")

# 3. Пользовательские числа
user_numbers = []
for i in range(5):
    user_numbers.append(int(input(f"Введите число {i+1}: ")))
user_numbers.sort()
print(f"Отсортированный список: {user_numbers}")

# 4. Удаление дубликатов
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print(f"\n4. Список без дубликатов: {unique_list}")

# 5. Поменять местами первый и последний
if len(numbers) > 1:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(f"\n5. После замены первого и последнего: {numbers}")


#  СЛОВАРИ

# 1. Словарь студентов
students = {"Иван": 4, "Мария": 5, "Петр": 3, "Анна": 4}
average = sum(students.values()) / len(students)
print(f"1. Средний балл студентов: {average:.2f}")

# 2. Количество букв в строке
text = input("\n2. Введите строку: ")
letter_count = {}
for char in text:
    if char != " ":
        letter_count[char] = letter_count.get(char, 0) + 1
print(f"Количество букв: {letter_count}")

# 3. Квадраты чисел
squares = {i: i*i for i in range(1, 11)}
print(f"\n3. Квадраты чисел: {squares}")

# 4. Словарь из двух списков
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined_dict = dict(zip(keys, values))
print(f"\n4. Словарь из списков: {combined_dict}")

#  МНОЖЕСТВА

# 1. Пересечение и объединение
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"1. Множество 1: {set1}")
print(f"   Множество 2: {set2}")
print(f"   Пересечение: {set1 & set2}")
print(f"   Объединение: {set1 | set2}")

# 2. Уникальные слова
text = input("\n2. Введите текст: ")
words = text.split()
unique_words = set(words)
print(f"Уникальные слова: {unique_words}")

# 3. Общие элементы
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"\n3. Общие элементы: {common}")

# 4. Подмножество
print(f"\n4. set1 является подмножеством set2: {set1.issubset(set2)}")

# 5. Удаление элементов
num_set = {1, 5, 10, 15, 20}
threshold = 10
filtered_set = {x for x in num_set if x >= threshold}
print(f"\n5. Множество после фильтрации: {filtered_set}")

#  КОМБИНИРОВАННЫЕ ЗАДАНИЯ

# 1. Уникальные случайные числа
random_list = [random.randint(1, 20) for _ in range(20)]
unique_random = list(set(random_list))
print(f"1. Уникальные значения: {unique_random}")

# 2. Счётчик элементов
count_dict = {}
for num in random_list:
    count_dict[num] = count_dict.get(num, 0) + 1
print(f"\n2. Количество повторений: {count_dict}")

# 3. Слова длиной > 5 символов
words_list = ["apple", "banana", "cat", "dog", "elephant"]
long_words = {word for word in words_list if len(word) > 5}
print(f"\n3. Слова длиной > 5: {long_words}")

# 4. Количество вхождений слов
sentence = input("\n4. Введите предложение: ")
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"Количество вхождений слов: {word_count}")

# 5. Удаление дубликатов через множество
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))
print(f"\n5. Без дубликатов: {unique_list}")

# 6. Самый дорогой товар
products = {"яблоко": 50, "банан": 30, "апельсин": 80, "виноград": 120}
most_expensive = max(products, key=products.get)
print(f"\n6. Самый дорогой товар: {most_expensive} ({products[most_expensive]} руб.)")

# 7. Частые имена
names = ["Иван", "Мария", "Иван", "Петр", "Мария", "Мария"]
name_count = {}
for name in names:
    name_count[name] = name_count.get(name, 0) + 1

most_common = max(name_count, key=name_count.get)
repeated_names = [name for name, count in name_count.items() if count > 1]

print(f"\n7. Имена, встречающиеся более 1 раза: {repeated_names}")
print(f"   Самое частое имя: {most_common}")

# 8. Первое вхождение символов
text = input("\n8. Введите строку: ")
first_occurrence = {}
for index, char in enumerate(text):
    if char not in first_occurrence:
        first_occurrence[char] = index
print(f"Первое вхождение символов: {first_occurrence}")