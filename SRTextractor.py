#!/usr/bin/env python

# Author: Jon Jackson
# Created: Jan 5, 2018

# This automation program goes through a pre-defined directory, scanning for mp4s with

import ffmpy, os, subprocess
from subprocess import check_output  # get a string from ffprobe subtitle_check
from os import path
from shutil import copyfile

# GLOBAL CONSTANTS
DIR = '.'                 # target directory to run through
CHAR_CUT = -4             # how many character to cut off (i.e. ".mp4" is -4
ARGS = ['-map','0:s:0','-loglevel','panic' ]  # arguments/options to implement when creating new OUTPUT file
ADD_TO_NAME = ".en.srt"   # after .mp4 is removed, add this to filename


def run_FFMPEG_extractor_through_pwd(DIR):
    for file in os.listdir(DIR):       # for every file in current directory
        if file.endswith('mp4'):       # if the file is an .mp4

            run_ffmpeg_on_file(file)   # save the mp4's caption as an .srt.. or whatever other arguments User wants (see top)
            return file



# Implements FFMPEG arguments on $targetFile
def run_ffmpeg_on_file(file):

    fileNEW = newName(file)

    # if $file exists in pwd, delete original version of file
    if os.path.isfile(fileNEW):
        os.remove(fileNEW)


    ff = ffmpy.FFmpeg(                  # calls FFMPEG from ffmpy module
        inputs = { file : None},        # call original INPUT $file
        outputs = { fileNEW : ARGS}     # adjust name and implement arguments/options
    )
    ff.run()                            # creates OUTPUT file


# Splice .mp4 out of name during new file creatio   n
def newName(file):
    cutName = file[:-4]       # make a new string based on .mp4 being cut
    return cutName+ADD_TO_NAME    # add whatever the User wants to filename


def copy_srt_without_tags(file):
    myIn = open(file, 'r')
    myOut = open(file + "NEW.rtf", 'w')

    for line in myIn:
        line = line.replace('<font size="24">', '')
        line = line.replace('</font>', '')
        line = line.replace('<font face="Arial">', '')
        myOut.write(line)

    myIn.close()
    myOut.close()

    os.remove(file)
    copyfile(file + "NEW.rtf", file)
    os.remove(file + "NEW.rtf")

def main():

    #confirm subitle exists
    #if (['ffprobe',''-v','error','-select_streams'',' s:0',' -show_entries','stream=codec_name','-of','default=noprint_wrappers=1:nokey=1',file)

    try:


        file = run_FFMPEG_extractor_through_pwd(DIR)# run FFMPEG on all files in pwd

        subType = subprocess.Popen(['/usr/bin/ffprobe','-v','error','-select_streams','s:0','-show_entries',\
                                    'stream=codec_name','-of','default=noprint_wrappers=1:nokey=1',file]).communicate()[0]
        if subType == "mov_text":
            file = newName(file)
            copy_srt_without_tags(file)
            print(subType + "works")


    except RuntimeError:
        print("runtime error, there may not be subtitles in " + '"' + file + '"')

    #something else happens, like the filename is still passed to make a SRT file
    except:
        #print("something bad happened... are you *sure* these all have subtitles?")
        print("looks like " + file + " has a problem.")

    print("yep, should be finished right about....now. Check out your new SRT files!")

#re-align filename with what was used in FFMPEG, for file-naming convention
main()
