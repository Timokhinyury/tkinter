import tkinter as tk
from tkinter import *
from math import sqrt
from tkinter import scrolledtext
from random import randint
from array import *


class Lesson1(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.label1 = Label(self, text="Введите 1 число:", bg="gold")
        self.label2 = Label(self, text="Введите 2 число:", bg="gold")
        self.label3 = Label(self, text="Введите 3 число:", bg="gold")
        self.label1.grid(row=0, column=0, sticky="w")
        self.label2.grid(row=1, column=0, sticky="w")
        self.label3.grid(row=2, column=0, sticky="w")

        self.entry1 = tk.Entry(self, width=6, justify=CENTER)
        self.entry2 = tk.Entry(self, width=6, justify=CENTER)
        self.entry3 = tk.Entry(self, width=6, justify=CENTER)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)
        self.entry3.grid(row=2, column=1, padx=5, pady=5)

        self.message_button = tk.Button(self, text="Посчитать", bg="gold", command=self.click_11)
        self.message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")
        self.label4 = tk.Label(self)
        self.label4.grid(row=5, column=0, sticky="w")

    def click_11(self):
        number_11 = self.entry1.get()
        number_22 = self.entry2.get()
        number_33 = self.entry3.get()
        h = sqrt(((int)(number_11) ** 2) + ((int)(number_22) ** 2))
        if h > (int)(number_33):
            result_1 = "точка находится за пределами круга"
        else:
            result_1 = " точка принадлежит кругу"
        self.label4.configure(text=result_1, bg="gold", font="bold")

class Lesson2(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.message_button = tk.Button(self, text="Посчитать", command=self.Namber_11)
        self.message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

        self.txt = scrolledtext.ScrolledText(self, width=20, height=10)

        self.label1 = tk.Label(self, text="Введите 1 число:")
        self.label1.grid(row=0, column=0, sticky="w")
        self.entry = tk.Entry(self, width=6, justify=CENTER)
        self.entry.grid(row=0, column=1, padx=5, pady=5)
        self.label4 = tk.Label(self)
        self.label4.grid(row=5, column=0, sticky="w")
        self.txt.grid(row=5, padx=5, pady=5, columnspan=5)

    def Namber_11(self):
        self.txt.delete(1.0, END)
        number_11 = self.entry.get()
        sum = 0
        for char in number_11:
            sum += int(char)
        self.txt.insert(INSERT, sum)

class Lesson3(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.label1 = Label(self, text="Введите 1 число:", bg="gold")
        self.label2 = Label(self, text="Введите 2 число:", bg="gold")
        self.label3 = Label(self, text="Введите 3 число:", bg="gold")
        self.label1.grid(row=0, column=0, sticky="w")
        self.label2.grid(row=1, column=0, sticky="w")
        self.label3.grid(row=2, column=0, sticky="w")
        self.entry1 = tk.Entry(self, width=6, justify=CENTER)
        self.entry2 = tk.Entry(self, width=6, justify=CENTER)
        self.entry3 = tk.Entry(self, width=6, justify=CENTER)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)
        self.entry3.grid(row=2, column=1, padx=5, pady=5)
        self.message_button = tk.Button(self, text="Посчитать", bg="gold", command=self.click_11)
        self.message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")
        self.label4 = tk.Label(self)
        self.label4.grid(row=5, column=0, sticky="w")

    def click_11(self):
        number_11 = self.entry1.get()
        number_22 = self.entry2.get()
        number_33 = self.entry3.get()
        P = (((int)(number_22))) * (((int)(number_22)))
        R = sqrt((int)(number_11) / 3.14)
        if R >= (((int)(number_22) ** 2) + ((int)(number_33) ** 2)) / 4:
            result_1 = "Прямоугольник находится внутри окружности"
        else:

            if R <= (int)(number_22) / 2 and R <= (int)(number_33) / 2:
                result_1 = "Окружность находится внутри прямоугольника"
            else:
                result_1 = "Окружность и прямоугольник не поместятся друг в друга"
        self.label4.configure(text=result_1)

class Lesson4(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.message_button = Button(self, text="Посчитать", bg="plum", command=self.sum_2)
        self.message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")
        self.label1 = Label(self, text="Введите 1 число:", bg="plum")
        self.label2 = Label(self, text="Введите 2 число:", bg="plum")
        self.label4 = Label(self)
        self.label1.grid(row=0, column=0, sticky="w")
        self.label2.grid(row=1, column=0, sticky="w")
        self.label4.grid(row=2, column=0, sticky="w")
        self.entry1 = Entry(self, width=6, justify=CENTER)
        self.entry2 = Entry(self, width=6, justify=CENTER)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

    def sum_2(self):
        number_11 = self.entry1.get()
        number_22 = self.entry2.get()
        result_1 = ("Сумма равна"), (((int)(number_11)) + ((int)(number_22)))
        self.label4.configure(text=result_1, bg="yellow", font="bold")

class Lesson5(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.message_button = Button(self, text="Посчитать", command=self.func)
        self.message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")
        self.txt = scrolledtext.ScrolledText(self, width=20, height=10)
        self.label1 = Label(self, text="Введите 1 число:")
        self.label2 = Label(self,text="Введите 2 число:")
        self.label1.grid(row=0, column=0, sticky="w")
        self.label2.grid(row=1, column=0, sticky="w")
        self.entry1 = Entry(self, width=6, justify=CENTER)
        self.entry2 = Entry(self, width=6, justify=CENTER)
        self.entry1.insert(0, '10')
        self.entry2.insert(0, '10')
        self.entry1.grid(row=0, column=1, padx=5, pady=5)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)
        self.txt.grid(row=5, padx=5, pady=5, columnspan=5)

    def func(self):
        for n in range(1, (int)(self.entry1.get())):
            for m in range(1, (int)(self.entry2.get())):
                if (60000 + 7000 + m * 100 + 10 + n) % 36 == 0:
                    self.txt.insert(INSERT, (60000 + 7000 + m * 100 + 10 + n))
                    self.txt.insert(INSERT, '\n')

class Lesson6(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.message_button = Button(self, text="Посчитать", command=self.click_11)
        self.message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")
        self.txt = scrolledtext.ScrolledText(self, width=20, height=10)
        self.label1 = Label(self, text="Введите 1 число:")
        self.label2 = Label(self,text="Введите 2 число:")
        self.label1.grid(row=0, column=0, sticky="w")
        self.label2.grid(row=1, column=0, sticky="w")
        self.entry1 = Entry(self, width=6, justify=CENTER)
        self.entry2 = Entry(self, width=6, justify=CENTER)
        self.entry1.insert(0, '5')
        self.entry2.insert(0, '5')
        self.entry1.grid(row=0, column=1, padx=5, pady=5)
        self.entry2.grid(row=1, column=1, padx=5, pady=5)
        self.txt.grid(row=5, padx=5, pady=5, columnspan=5)

    def click_11(self):

        mtx = []
        self.txt.delete(1.0, END)
        for i in range(0, (int(self.entry1.get()))):
            a = []
            for j in range(0, (int(self.entry2.get()))):
                a.append(randint(1, 10))
            mtx.append(a)
        for i in range(0, (int(self.entry1.get()))):
            self.txt.insert(INSERT, '\n')
            for j in range(0, (int(self.entry2.get()))):
                self.txt.insert(INSERT, mtx[i][j])
                self.txt.insert(INSERT, ' ')

        k = 0
        self.txt.insert(INSERT, '\n')
        for j in range(0, (int(self.entry1.get()))):
            for i in range(0, (int(self.entry2.get()))):
                self.txt.insert(INSERT, mtx[i][j])
                self.txt.insert(INSERT, ' ')


class Lesson7(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.min_price = [10, 5, 20, 10, 5, 5]
        self.magaz = [[10, 15, 20, 20, 15, 15], [10, 5, 30, 15, 15, 15], [10, 15, 20, 10, 15, 15], [12, 5, 21, 11, 5, 5]]
        self.message_button = Button(self, text="Посчитать", command=self.func)
        self.message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

        self.title("Задание 7")
        self.txt = scrolledtext.ScrolledText(self, width=20, height=10)
        self.txt1 = scrolledtext.ScrolledText(self, width=20, height=10)

        self.label3 = Label(self, text="Минимальная цена:")
        self.label3.grid(row=0, column=0)
        self.label4 = Label(self, text=(str)(self.min_price[0]) + ' ' + (str)(self.min_price[1]) + ' ' + (str)(self.min_price[2]) + ' ' + (str)(
            self.min_price[3]) + ' ' + (str)(self.min_price[4]) + ' ' + (str)(self.min_price[5]))
        self.label4.grid(row=0, column=1)

        self.txt.grid(row=5, padx=5, pady=5, columnspan=5)
        self.txt1.grid(row=7, padx=5, pady=5, columnspan=5)
        for i in range(0, 4):
            self.txt.insert(INSERT, "\n")
            for j in range(0, 6):
                self.txt.insert(INSERT, self.magaz[i][j])
                self.txt.insert(INSERT, " ")

        self.label5 = Label(self, text="")

    def func(self):
        self.txt1.delete(1.0, END)
        for data in self.magaz:
            count = 0
            for i in range(0, len(self.min_price)):
                if self.min_price[i] == data[i]:
                    count = count + 1
                    if count > 2:
                        self.txt1.insert(INSERT, "Магазин" + (str)(data) + "имеет более 2 товаров по минимальной цене")
                        self.txt1.insert(INSERT, "\n")

class Lesson8(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.message_button = Button(self, text="Посчитать", command=self.click_11)
        self.message_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")
        self.title("Задание 8")
        self.txt = scrolledtext.ScrolledText(self, width=20, height=10)
        self.label1 = Label(self, text="Введите строку:")
        self.label2 = Label(self, text="Результат:")
        self.label1.grid(row=0, column=0, sticky="w")
        self.label2.grid(row=1, column=0, sticky="w")
        self.entry1 = Entry(self, width=20, justify=CENTER)
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

    def click_11(self):
        s = self.entry1.get()
        # замена aa на ay
        s.replace("aa", "ay")
        self.label2.configure(text="Результат: " + s.replace("aa", "ay"))

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn1 = tk.Button(self, text="Задание 1",
                              command=self.open_window_1)
        self.btn1.pack(padx=50, pady=10)

        self.btn2 = tk.Button(self, text="Задание 2", command=self.open_window_2)
        self.btn2.pack(padx=50, pady=10)

        self.btn3 = tk.Button(self, text="Задание 3", command=self.open_window_3)
        self.btn3.pack(padx=50, pady=10)

        self.btn4 = tk.Button(self, text="Задание 4", command=self.open_window_4)
        self.btn4.pack(padx=50, pady=10)

        self.btn5 = tk.Button(self, text="Задание 5", command=self.open_window_5)
        self.btn5.pack(padx=50, pady=10)

        self.btn6 = tk.Button(self, text="Задание 6", command=self.open_window_6)
        self.btn6.pack(padx=50, pady=10)

        self.btn7 = tk.Button(self, text="Задание 7", command=self.open_window_7)
        self.btn7.pack(padx=50, pady=10)

        self.btn8 = tk.Button(self, text="задание 8", command=self.open_window_8)
        self.btn8.pack(padx=50, pady=10)

        self.btn9 = tk.Button(self, text="Задание 9", command=self.open_window_9)
        self.btn9.pack(padx=50, pady=10)

        self.btn10 = tk.Button(self, text="Задание 10", command=self.open_window_10)
        self.btn10.pack(padx=50, pady=10)

    def open_window_1(self):
        lesson_2 = Lesson1(self)
        lesson_2.grab_set()

    def open_window_2(self):
        lesson_2 = Lesson2(self)
        lesson_2.grab_set()

    def open_window_3(self):
        lesson_3 = Lesson3(self)
        lesson_3.grab_set()

    def open_window_4(self):
        lesson_4 = Lesson4(self)
        lesson_4.grab_set()

    def open_window_5(self):
        lesson_5 = Lesson5(self)
        lesson_5.grab_set()

    def open_window_6(self):
        lesson_6 = Lesson6(self)
        lesson_6.grab_set()

    def open_window_7(self):
        lesson_7 = Lesson7(self)
        lesson_7.grab_set()

    def open_window_8(self):
        lesson_8 = Lesson8(self)
        lesson_8.grab_set()

    def open_window_9(self):
        lesson_2 = Lesson2(self)
        lesson_2.grab_set()

    def open_window_10(self):
        lesson_2 = Lesson2(self)
        lesson_2.grab_set()

if __name__ == "__main__":
    app = App()
    app.mainloop()
