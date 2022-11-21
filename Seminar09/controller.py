import SaveYouTube

def clicked(e, lis, btn1, e1):
    # global quality
    global r
    btn1.grid(column=0, row=3)
    value = e.get()
    data = SaveYouTube.ytube(value)
    
    r = [(str(i)).split() for i in data]
    for i in r:
        lis.insert('end', i[3:5])
        print(i)
    lis.grid(row=2, column=2, rowspan=3)
    # print(r)
    # quality = lis.curselection()
    # print(quality)

def clicked_save(lis_quality, lis):
    val_listbox = lis.curselection()
    val = val_listbox[0]
    # print(lis_quality)
    itag = str(r[val][1][6:-1])
    file_extension = "." + str(r[val][2][r[val][2].find('/')+1:-1])
    print(itag, file_extension)
    # print(val_listbox[0])
    # print(r[val])
    # print(r[val][1][6:-1])
    # print(r[val][2][r[val][2].find('/')+1:-1])


# ['<Stream:', 'itag="17"', 'mime_type="video/3gpp"', 'res="144p"', 'fps="6fps"', 'vcodec="mp4v.20.3"',
# 'acodec="mp4a.40.2"', 'progressive="True"', 'type="video">']