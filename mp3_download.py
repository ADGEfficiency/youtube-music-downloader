#!/usr/bin/env python3
import argparse
from pytube import YouTube
parser = argparse.ArgumentParser()
parser.add_argument('url', default="", nargs='?')
parser.add_argument('fname', default="", nargs='?')
args = parser.parse_args()
url = args.url
fname = args.fname
yt = YouTube(url)
yt.streams.filter().filter(only_audio=True).order_by('abr')[-1].download(filename=fname)
