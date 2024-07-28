import yt_dlp


url = input('Informe a url do vídeo que deseja fazer o download: ').strip()

if url:

    video_url = url

    ydl_opts = {
        'format': 'best',  
        'outtmpl': '%(title)s.%(ext)s',  
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download concluído!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

else:
    print('Link inválido...')

