from tkinter import *
import controller


window = Tk()
window.title("Приложение для скачивания с YouTube")
window.geometry('800x250')
lbl = Label(window, text="Вставьте ссылку с канала.", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

lbl1 = Label(window)
lbl1.grid(column=0, row=1)

btn = Button(window, text="Проверка", command=lambda: controller.clicked(e, lbl1))
btn.grid(column=0, row=3)

e = Entry(window, width=100, borderwidth=5)
e.grid(row=0, column=2, columnspan=3, padx=10, pady=10)



window.mainloop()

