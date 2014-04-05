Youtube to MP3
==============

This project was created for help download videos from youtube, using playlist file on .txt format like input (this can be improved on future for read other type files)

Dependencies step-by-step
-----------------
>1. Python 2.7 or more
>2. Gdata.Youtube - https://code.google.com/p/gdata-python-client/downloads/list
>3. You need install *ffmge*
> ```sh
sudo apt-get install ffmpeg libavcodec-extra-53
```
>4. You need install *youtube-dl* - http://rg3.github.io/youtube-dl/download.html

How use
-----------------
```sh
git clone https://github.com/jgabriellima/youtube_to_mp3.git
python youtube.py
```

Change dataset name on code

- Use below code for dataset read  and get youtube video address

```sh
youtube = YoutubeDownload('dataset/dataset.txt','\t')
youtube.run()
```

- Use below code for dataset read, get youtube video address and download videos on .mp3 format


```sh
youtube = YoutubeDownload('dataset/dataset.txt','\t')
youtube.run_download_mp3()
youtube.convertM4aToMp3()
```

Adverts
--------
1. This code just was tested on Ubuntu
2. Study, learn, change, improve and share!

Contacts
-------------
* [J. Gabriel Lima] - visit my website [http://jgabriellima.com]
* Gtalk: jgabriel.ufpa
* Skype: jgabriel.lima
* Twitter: jgabriel_lima

[J. Gabriel Lima]:http://jgabriellima.com
[http://jgabriellima.com]:http://jgabriellima.com




