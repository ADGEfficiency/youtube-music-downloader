# youtube-music-downloader

Small wrapper around `pytube` to download mp3's from YouTube.

## Setup

Setup the wrapper:

```bash
$ git clone https://github.com/ADGEfficiency/youtube-music-downloader
$ cd youtube-music-downloader
$ chmod +x pytube-wrapper
```

Install `pytube`:

```bash
$ git clone https://github.com/nficano/pytube
$ cd pytube
$ python setup.py install
```

We use `ffmpeg` to convert from `.webm` to `.mp3`:

```bash
$ brew install ffmpeg
```

## Use

Make sure you keep spaces out of FILENAME!

```bash
./pytube-wrapper URL FILENAME
```

For example:
```bash
./pytube-wrapper https://www.youtube.com/watch?v=yZOhtyTyqBw not-what-is-alan-watts
```

Will download to a file `not-what-is-alan-watts.mp3`
