# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
# from tkinter import *


# def clicked(btn1, x, y):
#     global count
#     btn1["state"] = DISABLED
#     if count % 2 == 0:
#         btn1['text'] = 'X'
#     else:
#         btn1['text'] = 'O'
#     btn1["state"] = DISABLED
#     count += 1
#     a = btn1['text']
#     btn[x][y] = a

#     if btn[0][0] == a and btn[0][1] == a and btn[0][2] == a or (
#             btn[1][0] == a and btn[1][1] == a and btn[1][2] == a or
#             btn[2][0] == a and btn[2][1] == a and btn[2][2] == a or
#             btn[0][0] == a and btn[1][0] == a and btn[2][0] == a or
#             btn[0][1] == a and btn[1][1] == a and btn[2][1] == a or
#             btn[0][2] == a and btn[1][2] == a and btn[2][2] == a or
#             btn[0][0] == a and btn[1][1] == a and btn[2][2] == a or
#             btn[0][2] == a and btn[1][1] == a and btn[2][0] == a):
#         l1 = Label(text=f'Победили "{a}", УРААААА!!!!')
#         l1.grid(column=4, row=4)
#         for i in range(3):
#             for j in range(3):
#                 if btn[i][j] != 'X' and btn[i][j] != 'O':
#                     btn[i][j]['state'] = DISABLED


# btn = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# count = 0
# window = Tk()
# window.title('"крестики-нолики"')
# window.geometry('400x250')

# for i in range(3):
#     for j in range(3):
#         btn[i][j] = Button(window, text='', command=lambda x=i,
#                            y=j: clicked(btn[x][y], x, y), width=4)
#         btn[i][j].grid(column=j, row=i)
# window.mainloop()
