from random import *
import tkinter as tk
import math
import time

# Создание экрана
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

# Классы

class Ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
            x - начальное положение мяча по горизонтали
            y - начальное положение мяча по вертикали
            r - радиус шара
            vx - начальная скорость шара по горизонтали
            vy - начальная скорость шара по вертикали
            dt - дифференциал времени для шара
            g - ускорение свободного падения, действующая на шар
            live - начальное кол-во жизней шара
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.dt = 1
        self.g = 5
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def kill(self):
        """Время жизни шарика.

        Метод уменьшает кол-во очков жизни шарика на единицу за одну итерацию.
        """
        if int(self.vx) == 0 and int(self.vy) == int(self.g * self.dt):
            self.live -= 1

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        canv.delete(self.id)
        if 0 >= self.x - self.r or self.x + self.r >= 800:
            self.vx = - self.vx
            self.x += self.vx * self.dt
        elif 0 >= self.y - self.r or self.y + self.r >= 600:
            self.vy = -self.vy
            self.y += self.vy * self.dt + self.g * (self.dt ** 2) / 2
            self.vy = (self.vy + self.g * self.dt) / 2
            self.vx = self.vx / 2
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt + self.g * (self.dt ** 2) / 2
        self.vy = self.vy + self.g * self.dt
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def hit_test(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self):
        """ Конструктор класса gun

        Args:
            f2_power - начальная мощность выстрела шара
            f2_on - заряд пушки
            an - начальный угол пушки
        """
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        """Начало зарядки пушки."""
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targeting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        """Наращивание мощности выстрела пушки."""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:
    def __init__(self):
        """Конструктор класса target.

        Args:
            points - начальное количество очков за попадание по мишени
            live - начальное кол-во жизней мишени
        """
        self.points = 0
        self.live = 1

    def move_targets(self):
        """Перемещение мишени по прошествии единицы времени.

        Метод описывает перемещение мишени за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy и стен по краям окна (размер окна 800х600).
        """
        canv.delete(self.id)
        if 0 >= self.x - self.r or self.x + self.r >= 800:
            self.vx = - self.vx
            self.x += self.vx * self.dt
        elif 0 >= self.y - self.r or self.y + self.r >= 600:
            self.vy = -self.vy
            self.y += self.vy * self.dt
        self.x += self.vx * self.dt
        self.y += self.vy * self.dt
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def new_target(self):
        """ Инициализация новой цели.

        Args:
            x - начальное положение мишени по горизонтали
            y - начальное положение мишени по вертикали
            r - радиус мишени
            vx - начальная скорость мишень по горизонтали
            vy - начальная скорость мишень по вертикали
            dt - дифференциал времени для мишени
            g - ускорение свободного падения, действующая на мишень
         """
        self.x = randint(600, 740)
        self.y = randint(300, 540)
        self.r = randint(20, 50)
        self.vx = randint(5, 20) * (-1) ** (randint(1, 2))
        self.vy = randint(5, 20) * (-1) ** (randint(1, 2))
        self.dt = 1
        self.color = 'red'
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        canv.itemconfig(self.id, fill=self.color)

    def hit(self):
        """Попадание шарика в цель."""
        self.points += 1


# Создание объектов и глобальных переменных необходимых для запуска игры
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []
t1 = Target()
t2 = Target()
targets = [t1, t2]


def new_game():
    """Запуск игры.

    Создаем мишени с помощью метода new_target, после чего присваиваем мышке управление пушкой, отслеживая ее движение
    и нажатие кнопок с помощью команды canv.bind.
    Отслеживаем количество очков с помощью команды id_points, и пишем их значение в левом верхнем углу экрана.
    Затем шарики и мишени начинают двигаться или пропадать, в зависимости от того, выполнено то или иное условие.
    Ставим задержку на обновлени экрана в 0.03 секунды, чтобы объекты двигались не так быстро, а также даем пушке
    возможность усиливаться с помощью метода power_up.
    Если все мишени уничтожены, то высвечивается текст, в котором показано за какое количество выстрелов
    вы уничтожили мишени.
    """
    t1.new_target()
    t2.new_target()
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targeting)
    id_points = canv.create_text(30, 30, text=0, font='28')
    while Target().live or balls:
        for b in balls:
            canv.itemconfig(id_points, text=t1.points+t2.points)
            b.move()
            b.kill()
            if b.live == 0:
                b.move()
                canv.delete(b.id)
                balls.remove(b)
            elif b.hit_test(t2) and t2.live:
                t2.live = 0
                t2.hit()
                t2.move_targets()
                canv.delete(t2.id)
                targets.remove(t2)
            elif b.hit_test(t1) and t1.live:
                t1.live = 0
                t1.hit()
                t1.move_targets()
                canv.delete(t1.id)
                targets.remove(t1)
            elif len(targets) == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        for t in targets:
            t.move_targets()
        canv.update()
        time.sleep(0.03)
        g1.power_up()


# Иницилизация игры
new_game()
