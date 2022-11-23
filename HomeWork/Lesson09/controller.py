import SaveYouTube

def clicked(e, lis, btn1):
    global r
    btn1.grid(column=0, row=3)
    value = e.get()
    data = SaveYouTube.ytube(value)
    
    r = [(str(i)).split() for i in data]
    for i in r:
        lis.insert('end', i[3:5])
    lis.grid(row=2, column=2, rowspan=3, columnspan=10)

def clicked_save(lis, e1, e2):
    val_listbox = lis.curselection()
    val = val_listbox[0]
    itag = int(r[val][1][6:-1])
    file_extension = "." + str(r[val][2][r[val][2].find('/')+1:-1])
    file_name = f'{e2.get()}{file_extension}'
    path_save = e1.get()
    
    SaveYouTube.save_ytube (itag, file_name, path_save) 
    


