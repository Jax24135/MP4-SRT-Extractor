#!/usr/bin/env python

#JonMSG - KungFu adds "<font size>" messages... need to figure out how to rid these from output regEx?

import ffmpy, os
#from os import path
from shutil import copyfile

# GLOBAL CONSTANTS
DIR = '.'                 # target directory to run through
CHAR_CUT = -4             # how many character to cut off (i.e. ".mp4" is -4)
ARGS = ['-map','0:s:0','-loglevel','panic' ]  # arguments/options to implement when creating new OUTPUT file
ADD_TO_NAME = ".en.srt"   # after .mp4 is removed, add $this to filename

# Implements FFMPEG arguments on $targetFile
def run_ffmpeg_on_file(file):

    fileNEW = newName(file)

    #if file already exists, delete it... vanilla overwrite
    if os.path.isfile(fileNEW):
        os.remove(fileNEW)

    ff = ffmpy.FFmpeg(                      # calls FFMPEG from ffmpy module
            inputs = { file : None},        # call original INPUT $file
            outputs = { fileNEW : ARGS}     # adjust name and implement arguments/options
    )
    ff.run()                                # creates OUTPUT file

# Splice .mp4 out of name during new file creation
def newName(file):
    cutName = file[:-4]       # make a new string based on .mp4 being cut
    return cutName + ADD_TO_NAME    # add whatever the User wants to filename

def main():

    # run FFMPEG on all files in pwd - IF file ends in ".mp4"
    for file in os.listdir(DIR):             # for every file in current directory
        if file.endswith('mp4'):             # if the file is an .mp4
            run_ffmpeg_on_file(file)         # save the mp4's caption as an .srt.. or whatever other arguments User wants (see top)

    #re-align filename with
    file = newName(file)

    #if file.is_dir():
        #os.remove(file)

    myIn = open(file,'r')
    myOut = open(file+"NEW.rtf",'w')

    for line in myIn:
        line = line.replace('<font size="24">','')
        line = line.replace('\r<font size="24">','')
        line = line.replace('</font>' , '' )
        line = line.replace('</font>\r' , '' )
        line = line.replace('<font face="Arial">' , '')
        line = line.replace('\r<font face="Arial">' , '')
        myOut.write(line)

    myIn.close()
    myOut.close()

    os.remove(file)
    copyfile(file+"NEW.rtf",file)
    os.remove(file+"NEW.rtf")

    print('\n'+"finished w/o errors")


main()