# MP4 >> SRT, Extractor
Author Jon Jackson
Date Created: Jan 5, 2018

This script pulls an SRT subtitle stream from a muxed MP4 file (uses FFMPEG), can be used with CloneDVD mobile to rip VOBs > mux CC in Handbrake, and rip as clean SRT with *this* script. Currently goes through all .mp4 files in a directory and adds "*.en.srt" to each extracted file.

Written/Built using PyCharm on a x64 Ubuntu system.

Dependencies:
 - Python3.6
 - FFMPEG
 - FFMPY (use "$python3.6 -m pip install ffmpy" to overcome inconsistant library location issue)
 - Handbrake is nice to have
 - CloneDVDmobie
