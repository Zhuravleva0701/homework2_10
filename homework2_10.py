from threading import Thread

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        day = 0
        number_enemies = 100
        print(f'{self.name}, на нас напали!')
        while number_enemies > 0:
            day += 1
            number_enemies = number_enemies - self.power
            print(f'"{self.name} сражается {day} дней ..., осталось {number_enemies} воинов."')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()





