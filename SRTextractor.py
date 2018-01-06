#!/usr/bin/env python


import ffmpy, os, subprocess

CHAR_CUT = -4   # how many character to cut off (i.e. ".mp4" is -4
ARGS = ['-map','0:s:0']

def extractMe(file):
    ff = ffmpy.FFmpeg(  # calls FFMPEG to perform operation
            inputs={file: None},  # call original INPUT $file
            outputs={newName(file):ARGS}
    )
    ff.run()

def newName(file):
    newA = file[:CHAR_CUT]
    return newA+".en.srt"

def main():
    for file in os.listdir():  # for every file in current directory
        if file.endswith('mp4'):  # if the file is an .mp4
            extractMe(file)  # save the mp4's caption as an .srt


main()