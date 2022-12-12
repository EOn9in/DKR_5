from tkinter import *
from tkinter import messagebox
import random
import time


def file():
    with open('input.txt', 'w', encoding='utf-8') as file:
        for i in range(100):
            num = random.randint(-50, 51)
            file.write(str(num) + '\n')
    return file


def vstavki_sort():
    start = time.perf_counter()
    f = open('input.txt', encoding='utf-8')
    w = open("out.txt", "w", encoding='utf-8')
    alist = []
    for line in f:
        alist.append(line.rstrip())
    n = len(alist)
    mass = alist
    f.close()
    for i in range(1, len(mass)):
        temp = mass[i]
        j = i - 1
        while (j >= 0 and temp < mass[j]):
            mass[j + 1] = mass[j]
            j = j - 1
        mass[j + 1] = temp
    w.write(str(mass))
    w.close()
    stop = time.perf_counter()
    itog = stop - start
    print(itog)
    messagebox.showinfo('Время выполнения', 'Сортировки вставками по возрастанию',detail = f'{itog}')


def vstavki_sort_ub():
    start = time.perf_counter()
    f = open('input.txt', encoding='utf-8')
    w = open("out.txt", "w", encoding='utf-8')
    alist = []
    for line in f:
        alist.append(line.rstrip())
    n = len(alist)
    mass = alist
    f.close()
    for i in range(len(mass)):
        for j in range(n - i - 1):
            if mass[j] < mass[j + 1]:
                mass[j], mass[j + 1] = mass[j + 1], mass[j]
            i -= 1
    w.write(str(mass))
    w.close()
    stop = time.perf_counter()
    itog = stop - start
    print(itog)
    messagebox.showinfo('Время выполнения','Сортировка вставками по убыванию', detail = f'{itog}')


def quickSort():
    start = time.perf_counter()
    f = open('input.txt', encoding='utf-8')
    w = open("out.txt", "w")
    alist = []
    for line in f:
        alist.append(line.rstrip())
    mass = alist
    f.close()
    m = str(sorted(mass))
    w.write(m)
    w.close()
    stop = time.perf_counter()
    itog = stop - start
    print(itog)
    messagebox.showinfo('Время выполнения','Сортировка быстрым алгоритмом по возрастанию', detail = f'{itog}')


def quickSort_ub():
    start = time.perf_counter()
    f = open('input.txt', encoding='utf-8')
    w = open("out.txt", "w")
    alist = []
    for line in f:
        alist.append(line.rstrip())
    mass = alist
    f.close()
    m = str(sorted(mass, reverse=True))
    w.write(m)
    w.close()
    stop = time.perf_counter()
    itog = stop - start
    print(itog)
    messagebox.showinfo('Время выполнения','Сортировка быстрым алгоритмом по убыванию',detail =  f'{itog}')


def ExitApp():
    MsgBox = messagebox.askquestion('Выход из программы', 'Вы уверены, что хотите выйти?', icon='error')
    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('С возвращением!', 'Мы рады, что вы остались с нами!')


root = Tk()
root.title("Сортировки")
root.geometry("670x325")
root.attributes('-alpha', 0.95)

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

label = Label(frame, text='Задание (Вариант 12):', font=("Arial", 16))
label.pack()
label_1 = Label(frame, text='1.Реализовать сортировку данных с помощью вставок.\n'
                            '2.Реализовать сортировку данных с помощью быстрого алгоритма.\n'
                            '3.В обоих случаях необходимо предусмотреть возможность изменения компаратора \n(реализация компаратора в виде передаваемой в подпрограмму функции).\n'
                            '4.Считывание и вывод данных необходимо производить из текстового файла.\n'
                            '5.Для демонстрации работы программных реализаций самостоятельно подготовить варианты \n входных данных (при этом объём текстовых файлов должен позволять оценить скорость работы программ).',
                justify=LEFT, font=('Arial', 9))
label_1.pack()

button = Button(frame, text="Изменить числа в исходном файле", command=file)
button.pack()

btn = Button(frame, text='Сортировка вставками (по возрастанию)', command=vstavki_sort)
btn.pack(fill=X)

btnk = Button(frame, text='Сортировка вставками (по убыванию)', command=vstavki_sort_ub)
btnk.pack(fill=X)

butn = Button(frame, text='Быстрая сортировка (по возрастанию)', command=quickSort)
butn.pack(fill=X)

butnn = Button(frame, text='Быстрая сортировка (по убыванию)', command=quickSort_ub)
butnn.pack(fill=X)

buttonEg = Button(frame, text='Выход', command=ExitApp)
buttonEg.pack(anchor=SE)


def motionUP(event):
    children = frame.winfo_children()
    if event.widget in children:
        index = children.index(event.widget)
        index -= 1
        if index > -1:
            children[index].focus_set()


def motionDOWN(event):
    children = frame.winfo_children()
    if event.widget in children:
        index = children.index(event.widget)
        index += 1
        if index < len(children):
            children[index].focus_set()


root.bind('<Up>', motionUP)
root.bind('<Down>', motionDOWN)

root.mainloop()
