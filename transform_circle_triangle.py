import tkinter as tk
import numpy as np
import math

WIDTH = HEIGHT = 800

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=WIDTH, bg="grey50")
canvas.pack()

t = np.arange(math.pi/6, 13 * math.pi/6 + 0.02, 0.02)  # от пи/6 до 13ПИ/6 +0.02 с шагом 0.02
circle = []  # массив точек круга
for i in t:
    x = 400 + 200 * math.cos(i)
    y = 400 + 200 * math.sin(i)
    circle.append((x, y))

# строим круг-контур
x_start = circle[0][0]
y_start = circle[0][1]
for i in circle:
    x = i[0]
    y = i[1]
    canvas.create_line(x_start, y_start, x, y, width=1.5, fill="gray60")
    x_start = i[0]
    y_start = i[1]


def animation(a):

    if a == len(circle) - 1:
        canvas.create_line(circle[0][0], circle[0][1], circle[len(circle) // 3][0],
                           circle[len(circle) // 3][1], fill='RED', width=0.6)
        return

    v = round(len(circle) / 3)

    # на удачу определяем координаты вершины треугольника
    if 0 <= a <= v:  #  нижняя дуга (1/3)
        x_v = circle[0][0]
        y_v = circle[0][1]
    elif v < a <= 2 * v: #левая дуга (2/3)
        x_v = circle[v][0]
        y_v = circle[v][1]
    else:
        x_v = circle[2 * v][0]
        y_v = circle[2 * v][1]

    # стираем предыдущую красную линию
    canvas.delete("line")
    # закрашиваем точки окружности цветом фона


    if a in [v, 2 * v, len(circle)]: #1/3, 2/3, полный круг
        # рисуем сторону треугольника, если а попадает в вершину
        canvas.create_line(x_v, y_v, circle[a][0], circle[a][1], width=1.5, fill="red", tag="save")
    else:
        # рисуем удаляющиеся линии
        canvas.create_line(x_v, y_v, circle[a][0], circle[a][1], width=1.5, fill="red", tag="line")

    canvas.create_line(circle[a][0], circle[a][1], circle[a + 1][0], circle[a + 1][1],
                       width=5, fill="grey50")
    canvas.after(20, animation, a + 1) #вызывает функцию,
    # переданную вторым аргументом, через количество миллисекунд, указанных первым аргументом


if __name__ == '__main__':
    a = 0
    print(len(circle))
    animation(a)
    root.mainloop()
