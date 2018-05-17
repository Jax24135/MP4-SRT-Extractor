#!/usr/bin/env python

#JonMSG - finally removed pesky <HTML_TAGS>, is there a cleaner way to run through REPLACE list?

import ffmpy, os
#import os
#from ffmpy import FFmpeg
#from os import path
from shutil import copyfile

# GLOBAL CONSTANTS
DIR = '.'                 # target directory to run through
CHAR_CUT = -4             # how many character to cut off (i.e. ".mp4" is -4)
ARGS = ['-map','0:s:0','-loglevel','panic' ]  # arguments/options to implement when creating new OUTPUT file
ADD_TO_NAME = ".en.srt"   # after .mp4 is removed, add $this to filename

#HTML_TAGS = ['<font size="24">','\r<font size="24">','</font>','</font>\r','<font face="Arial">','<font face="Arial">\r']

def main():

    # run FFMPEG on all files in pwd - IF file ends in ".mp4"
    for file in os.listdir(DIR):                        # for every file in current directory
        if file.endswith('mp4'):                        # if the file is an .mp4.. do below
            newFile = file[:CHAR_CUT] + ADD_TO_NAME           # remove 'mp4 and add '.en.srt' to filename
            
            if os.path.isfile(newFile):                 # if the '.en.srt' file already exists
                os.remove(newFile)                      # delete previous SRT file
                
            ff = ffmpy.FFmpeg (
                inputs = { file : None },               # call original INPUT file
                outputs = { newFile : ARGS })           # save file as newFile and use global ARGuments
            
            ff.run()                                     # create the extracted SRT file
            
            #if file.is_dir():                          # JonMSG - not sure what this is...
            #   os.remove(file)


            
            myIn = open(newFile , 'r')
            myOut = open(newFile +".tmp.rtf" , 'w')

            for line in myIn:
                #line = line.replace(HTML_TAGS, '')
                line = line.replace('<font size="24">', '')
                line = line.replace('\r<font size="24">', '')
                line = line.replace('</font>', '')
                line = line.replace('</font>\r', '')
                line = line.replace('<font face="Arial">', '')
                line = line.replace('\r<font face="Arial">', '')
                myOut.write(line)

            myIn.close()
            myOut.close()

            #  folder cleanup

            #os.remove(file)                        # JonMSG - why delete the original file? (in case a VOB.tmp file)
            copyfile(newFile+".tmp.rtf",newFile)       # copy new file name into original filename spot
            os.remove(newFile+".tmp.rtf")           # remove file name with "NEW" tag  #decluttering


print('\n'+"finished w/o errors")  # confirm clean exit

main()