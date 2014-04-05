Youtube to MP3
==============

This project was created for help download videos from youtube, using playlist file on .txt format like input (this can be improved on future for read other type files)

Dependencies
-----------------
>1. Python 2.7
>2. Gdata.Youtube - https://developers.google.com/youtube/code?csw=1#Python
>3. Pytube - https://github.com/ablanco/python-youtube-download


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
```


[Gdata.Youtube]:http://gdata-samples-youtube-search-py.appspot.com/


