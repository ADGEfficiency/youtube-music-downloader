#!/usr/bin/env bash
mkdir -p ./music
url=$1
fname=$2
echo "starting download of $fname from $url"
python3 mp3_download.py $url $fname
fname="music/$fname.webm"
mv *.webm $fname
ffmpeg -i ${fname} -vn -ab 128k -ar 44100 -y "${fname%.webm}.mp3"
echo "cleaning up .webm"
rm ./music/*.webm
