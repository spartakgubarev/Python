from pytube import YouTube


PATH = input('Введите ссылку скачиваемого видео: ')
# PATH = 'https://www.youtube.com/watch?v=GP6F0y3eU0Q'
yt = YouTube(
    PATH,
    #on_progress_callback=progress_func,
    #on_complete_callback=complete_func,
    #proxies=my_proxies,
    use_oauth=False,
    allow_oauth_cache=True
    )

# print(yt.streams.filter(progressive=True), sep='\n')       # filter(progressive=True) - фильтр прогрессивных поток (только аудио и видео вместе)
for i in yt.streams.filter(progressive=''):
    print(i)
# print(yt.streams[0])


save_puth = input('Введите путь для сохранения: ')
stream = yt.streams.get_by_itag(22)     # качество видео
file_name = input('Введите название файла: ')
stream.download(save_puth, file_name + '.mp4')          # сохранить с указанием пути и названием файла
