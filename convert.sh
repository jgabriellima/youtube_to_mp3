#!/bin/bash
for i in *.m4a
do
ffmpeg -i "$i" -ab 256k "${i%m4a}mp3"
done