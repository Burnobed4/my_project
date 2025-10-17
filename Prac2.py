# 1. Декоратор логирования
def logger(func):
    def wrapper(*args):
        print(f"Вызов функции {func.__name__} с аргументами {args}")
        result = func(*args)
        print(f"Функция {func.__name__} вернула {result}")
        return result

    return wrapper


# Применение декоратора к функциям
@logger
def add(a, b):
    return a + b


@logger
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"


@logger
def greet(name):
    return f"Привет, {name}!"


# 2. Декоратор доступа
def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user, *args):
            if user.get('role') in allowed_roles:
                return func(user, *args)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
                return None

        return wrapper

    return decorator


# Пример использования
@require_role(['admin'])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")


@require_role(['admin', 'manager'])
def edit_settings(user):
    print(f"Настройки изменены пользователем {user['name']}")


# Тестирование
if __name__ == "__main__":
    print("Декоратор логирования:")
    print(add(5, 3))
    print(divide(10, 2))
    print(divide(10, 0))
    print(greet("Анна"))

    print("\nДекоратор доступа:")
    users = [
        {'name': 'Павел', 'role': 'admin'},
        {'name': 'Виктория', 'role': 'manager'},
        {'name': 'Александр', 'role': 'user'}
    ]

    for user in users:
        print(f"\nПользователь: {user['name']} (роль: {user['role']})")
        delete_database(user)
        edit_settings(user)