from tkinter import *

#функция вызывается кликом мышки по полю,
#проверяем, свободна ли клетка, осуществляем ход (первый игрок - X)
def click(row, col):
    global k
    global field_check
    global play
    if field[row][col]['text'] == ' ' and play == True:
        if k % 2 == 0:
            field[row][col]['text'] = 'X'
            field_check[row][col] = "X"
        else:
            field[row][col]['text'] = 'O'
            field_check[row][col] = "O"
        k += 1
        check()

#проверяем поле на выигрышную комбинацию, выводим оповещение об окончании игры
def check():
    global k
    global play
    m = 1 if k % 2 == 1 else 2
    m = str(m)
    if field_check[0][0] == field_check[0][1] == field_check[0][2]:
        play = False
        new_root = Tk()
        lb = Label(new_root, text="Игра окончена. Победил игрок " + m)
        lb.pack()
        new_root.mainloop()

    elif field_check[1][0] == field_check[1][1] == field_check[1][2]:
        play = False
        new_root = Tk()
        lb = Label(new_root, text="Игра окончена. Победил игрок " + m)
        lb.pack()
        new_root.mainloop()

    elif field_check[2][0] == field_check[2][1] == field_check[2][2]:
        play = False
        new_root = Tk()
        lb = Label(new_root, text="Игра окончена. Победил игрок " + m)
        lb.pack()
        new_root.mainloop()

    elif field_check[0][0] == field_check[1][0] == field_check[2][0]:
        play = False
        new_root = Tk()
        lb = Label(new_root, text="Игра окончена. Победил игрок " + m)
        lb.pack()
        new_root.mainloop()

    elif field_check[0][1] == field_check[1][1] == field_check[2][1]:
        play = False
        new_root = Tk()
        lb = Label(new_root, text="Игра окончена. Победил игрок " + m)
        lb.pack()
        new_root.mainloop()

    elif field_check[0][2] == field_check[1][2] == field_check[2][2]:
        play = False
        new_root = Tk()
        lb = Label(new_root, text="Игра окончена. Победил игрок " + m)
        lb.pack()
        new_root.mainloop()

    elif field_check[0][0] == field_check[1][1] == field_check[2][2]:
        play = False
        new_root = Tk()
        lb = Label(new_root, text="Игра окончена. Победил игрок " + m)
        lb.pack()
        new_root.mainloop()

    elif field_check[0][2] == field_check[1][1] == field_check[2][0]:
        play = False
        new_root = Tk()
        lb = Label(new_root, text="Игра окончена. Победил игрок " + m)
        lb.pack()
        new_root.mainloop()

    elif k == 9:
        play = False
        new_root = Tk()
        lb = Label(new_root, text="Игра окончена. Ничья")
        lb.pack()
        new_root.mainloop()

#создаём поле для проверки на выигрыш
play = True
k = 0
field_check = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#создаём окно
root = Tk()
root.title("Крестики-нолики")
field = []
#создаём кнопки
for i in range(3):
    line = []
    for j in range(3):
        button = Button(root, text=' ', width=4, height=2, font=('Colibri', 40, 'bold'), background='lightgreen',
                        command=lambda row=i, col=j: click(row, col))
        #добавляем кнопки в таблицу; sticky - размещает кнопку относительно ячейки по осям
        button.grid(row=i, column=j, sticky="nsew")
        line.append(button)
    field.append(line)
root.mainloop()
