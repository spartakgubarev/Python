from pytube import YouTube


def ytube(PATH):
    global yt
    yt = YouTube(
        PATH,
        #on_progress_callback=progress_func,
        #on_complete_callback=complete_func,
        #proxies=my_proxies,
        use_oauth=False,
        allow_oauth_cache=True
        )
    return yt.streams.filter(progressive='True')

def save_ytube(itag, file_name, path):
    stream = yt.streams.get_by_itag(itag)     # качество видео
    stream.download(path, file_name)          # сохранить с указанием пути и названием файла