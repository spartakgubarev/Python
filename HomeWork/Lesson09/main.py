from tkinter import *
import controller


window = Tk()
window.title("Приложение для скачивания с YouTube")
window.geometry('700x250')

lbl = Label(window, text="Ссылка:").grid(column=0, row=0)
lbl1 = Label(window, text="Куда сохранить:").grid(column=0, row=1)
lbl1 = Label(window, text="Имя файла:").grid(column=8, row=1)

btn = Button(window, text="Проверка", command=lambda: controller.clicked(e, lis, btn1))
btn.grid(column=0, row=2)

btn1 = Button(window, text="Скачать", command=lambda: controller.clicked_save(lis, e1, e2))
    
lis = Listbox(window, selectmode=SINGLE, height=4, width=100, yscrollcommand=5)

e = Entry(window, width=100)        # Пусть откуда качать
e.grid(row=0, column=2, columnspan=10)

e1 = Entry(window, width=60)        # Путь куда сохранить
e1.grid(row=1, column=2, columnspan=6)

e2 = Entry(window, width=25)        # Имя файла (без расширения)
e2.grid(row=1, column=10)

window.mainloop()
