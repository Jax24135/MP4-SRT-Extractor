#!/usr/bin/env python
import ffmpy, os, fileinput, codecs

# GLOBAL CONSTANTS
CHAR_CUT = -4           # how many character to cut off (i.e. ".mp4" is -4
ARGS = ['-map','0:s:0' ] # arguments/options to implement when creating new OUTPUT file
ADD_TO_NAME = ".en.srt" # after .mp4 is removed, add this to filename

# Implements FFMPEG arguments on $targetFile
def extractMe(file):
    ff = ffmpy.FFmpeg(                      # calls FFMPEG from ffmpy module
            inputs = { file : None},            # call original INPUT $file
            outputs = { newName(file) : ARGS}    # adjust name and implement arguments/options
    )
    ff.run()                                # creates OUTPUT file

# Splice .mp4 out of name during new file creation
def newName(file):
    cutName = file[:-4]       # make a new string based on .mp4 being cut
    return cutName+ADD_TO_NAME    # add whatever the User wants to filename

def main():

    for file in os.listdir():       # for every file in current directory
        if file.endswith('mp4'):    # if the file is an .mp4
            extractMe(file)         # save the mp4's caption as an .srt.. or whatever other arguments User wants (see top)

    myOut = open(file+"NEW.rtf",'w')

    with codecs.open(os.listdir(),"r",encoding="utf-8",errors="ignore"):

        for line in file:
                myOut.write(line)




    #myIn.close()
    myOut.close()

    #with fileinput.FileInput(file,inplace=True,backup=".bak") as file:
    #    for line in file:
    #        line.replace('<font size="24">' , '' , end='')
    #        line.replace('</font>' , '' , end='')
    #        line.replace('<font face="Arial">' , '', end='')

main()
