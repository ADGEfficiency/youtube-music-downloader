# youtube-music-downloader

Small wrapper around pytube to download mp3's from Youtube.

## Setup

`pip install pytube` gives me problems, instead install as below.  We use `ffmpeg` to convert from `.webm` to `.mp3`.

```bash
$ pip install git+https://gitlab.com/obuilds/public/pytube@ob-v1 --upgrade
$ brew install ffmpeg
$ chmod +x pytube-wrapper
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
