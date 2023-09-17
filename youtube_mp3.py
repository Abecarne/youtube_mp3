import youtube_dl

def download_video(url):
    ydl_opts = {
        'outtmpl': 'downloaded/%(title)s.mp3',
        'format': 'bestaudio/best',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == '__main__':
    url = input('Enter the url of the video you want to download: ')
    download_video(url)
