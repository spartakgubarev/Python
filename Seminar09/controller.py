import SaveYouTube


def clicked(e, lbl1):
    # lbl.configure(text="Я же просил...")
    value = e.get()
    data = SaveYouTube.ytube(value)
    
    a = [(str(i)).split() for i in data]

    
    lbl1.configure(text=[b[3] for b in a])
    e.grid(row=0, column=2, columnspan=3, padx=10, pady=10)