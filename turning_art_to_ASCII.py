# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 20:57:38 2021

@author: DELL
"""

#importing package 
import pywhatkit as pkt

#displaying a message
print("Turning to Images To ASCII Art")
#path to the image - here in same folder as of the current project file 
source_path = 'star.png'

#path to store the output, as it is an ASCII file, saving it with .text extension 
target_path = 'ascii_art.text'

#calling the inbuilt method of the module which converts the image to ASCII art, image_to_ascii_art(source_path,target_path) 
#by default the location of the ascii art image will be the same
pkt.image_to_ascii_art(source_path,target_path)