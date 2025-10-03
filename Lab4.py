class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Транспорт движется со скоростью {self.speed} км/ч")

    def __str__(self):
        return f"Транспорт: {self.brand}, Скорость: {self.speed}"


class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def honk(self):
        print("Би-Бип")

    def move(self):
        print(f"Автомобиль {self.brand} едет со скоростью {self.speed} км/ч")

    def __str__(self):
        return f"Автомобиль: {self.brand}, Скорость: {self.speed}, Мест: {self.seats}"

    def __len__(self):
        return self.seats

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False

    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        return NotImplemented


class Bike(Transport):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.type = bike_type

    def move(self):
        print(f"Велосипед {self.brand} едет со скоростью {self.speed} км/ч")

    def __str__(self):
        return f"Велосипед: {self.brand}, Скорость: {self.speed}, Тип: {self.type}"


# 4. Практика использования
transport1 = Transport("Обычный транспорт", 90)
car1 = Car("Субару", 260, 5)
car2 = Car("Додж", 220, 5)
bike1 = Bike("Волна", 25, "дорожный")

print("\nВывод объектов (__str__)")
print(transport1)
print(car1)
print(car2)
print(bike1)

print("\nПроверка методов move() и honk()")
transport1.move()
car1.move()
car1.honk()
bike1.move()

print("\nИспользование len(car)")
print(f"Количество мест в {car1.brand}: {len(car1)}")

print("\nСравнение двух машин (car1 == car2)")
print(f"car1 == car2: {car1 == car2}")

print("\nСложение скоростей двух машин (car1 + car2)")
print(f"Суммарная скорость: {car1 + car2}")

print("\nСложение машины и велосипеда (car1 + bike1)")
try:
    result = car1 + bike1
    print(f"Результат: {result}")
except TypeError as e:
    print(f"Ошибка: {e}")

# 5. Доп задание
print("\nДополнительное задание ")
vehicles = [
    Transport("Обычный транспорт", 60),
    Car("Ниссан", 150, 5),
    Car("Мерседес", 190, 4),
    Bike("Кама", 30, "шоссейный"),
    Bike("Урал", 20, "горный")
]

print("Список транспортных средств:")
for i in range(len(vehicles)):
    print(f"{i+1}. ", end="")
    vehicles[i].move()