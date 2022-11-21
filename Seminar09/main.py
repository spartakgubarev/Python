from tkinter import *
import controller


window = Tk()
window.title("Приложение для скачивания с YouTube")
window.geometry('700x250')


lbl = Label(window, text="Ссылка:").grid(column=0, row=0)

lbl1 = Label(window, text="Куда сохранить:")\
    .grid(column=0, row=1)

btn = Button(window, text="Проверка", command=lambda: controller.clicked(e, lis, btn1, e1))
btn.grid(column=0, row=2)

btn1 = Button(window, text="Скачать", command=lambda: controller.clicked_save(controller.r, lis))
    
lis = Listbox(window, selectmode=SINGLE, height=5, width=100, yscrollcommand=5)

e = Entry(window, width=100)
e.grid(row=0, column=2, columnspan=3)

e1 = Entry(window, width=100)
e1.grid(row=1, column=2, columnspan=3)

# print(controller.r)
window.mainloop()

# https://www.youtube.com/watch?v=CHhQb_mUNcU